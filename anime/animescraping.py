from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests


class animedealer():
    def __init__(self, query, animeid, episode_num, genre_name, page):  # Intialises the anime class
        self.query = query
        self.animeid = animeid
        self.episode_num = episode_num
        self.genre_name = genre_name
        self.page = page

    def get_search_results(query):
        try:
            url1 = f"https://gogoanime.cm//search.html?keyword={query}"
            session = HTMLSession()
            response = session.get(url1)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'html.parser')
            animes = soup.find("ul", {"class": "items"}).find_all("li")
            # print(animes)
            res_list_search = []
            for anime in animes:  # For every anime found
                tit = anime.a["title"]
                urll = anime.a["href"]
                r = urll.split('/')
                res_list_search.append({"name":f"{tit}","animeid":f"{r[2]}"})
            if res_list_search == []:
                return {"status":"204", "reason":"No search results found for the query"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}

    def get_anime_details(animeid):
        try:
            animelink = 'https://gogoanime.cm/category/{}'.format(animeid)
            session = HTMLSession()
            response = session.get(animelink)
            response_html = response.text
            soup = BeautifulSoup(response_html, "html.parser")
            # source_url = soup.find("div", {"class": "anime_info_body_bg"}).img
            # imgg = source_url.get('src')
            # tit_url = soup.find("div", {"class": "anime_info_body_bg"}).h1.string
            # lis = soup.find_all('p', {"class": "type"})
            # plot_sum = lis[1]
            # pl = plot_sum.get_text().split(':')
            # pl.remove(pl[0])
            # sum = ""
            # plot_summary = sum.join(pl)
            # type_of_show = lis[0].a['title']
            # ai = lis[2].find_all('a')  # .find_all('title')
            # genres = []
            # for link in ai:
            #     genres.append(link.get('title'))
            # year1 = lis[3].get_text()
            # year2 = year1.split(" ")
            # year = year2[1]
            # status = lis[4].a.get_text()
            # oth_names = lis[5].get_text()
            # lnk = soup.find(id="episode_page")
            # ep_str = str(lnk.contents[-2])
            # a_tag = ep_str.split("\n")[-2]
            # a_tag_sliced = a_tag[:-4].split(">")
            # last_ep_range = a_tag_sliced[-1]
            # y = last_ep_range.split("-")
            # ep_num = y[-1]
            # res_detail_search = {"title":f"{tit_url}", "year":f"{year}", "other_names":f"{oth_names}", "type":f"{type_of_show}", "status":f"{status}", "genre":f"{genres}", "episodes":f"{ep_num}", "image_url":f"{imgg}","plot_summary":f"{plot_summary}"}
            animename = str(soup.select('title'))[8:-9]
            last_ep = int(str(soup.select('a[href="\#"]')[1]).split()[2][8:-1])
            first_ep = int(str(soup.select('a[href="\#"]')[1]).split()[3][10:-1])
            img = soup.find("div", {"class":"anime_info_body_bg"}).img.get('src')
            return (last_ep, animename[:-13], img)
        # except AttributeError:
        #     return {"status":"400", "reason":"Invalid animeid"}
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection", 'str':' '}

    def get_episodes_link(animeid, episode_num):
        try:
            animelink = f'https://gogoanime.cm/{animeid}-episode-{episode_num}'
            session = HTMLSession()
            response = session.get(animelink, headers={'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'})
            response_html = response.text
            soup = BeautifulSoup(response_html, "html.parser")
            # animelink = f'https://gogoanime.cm/category/{animeid}'
            # response = requests.get(animelink)
            # plainText = response.text
            # soup = BeautifulSoup(plainText, "lxml")
            # lnk = soup.find(id="episode_page")
            # source_url = lnk.find("li").a
            # tit_url = soup.find("div", {"class": "anime_info_body_bg"}).h1.string
            # URL_PATTERN = 'https://gogoanime.cm/{}-episode-{}'
            # url = URL_PATTERN.format(animeid, episode_num)
            # srcCode = requests.get(url)
            # plainText = srcCode.text
            # soup = BeautifulSoup(plainText, "lxml")
            # source_url = soup.find("li", {"class": "dowloads"}).a
            # vidstream_link = source_url.get('href')
            # # print(vidstream_link)
            # URL = vidstream_link
            # dowCode = requests.get(URL)
            # data = dowCode.text
            # soup = BeautifulSoup(data, "lxml")
            # dow_url= soup.findAll('div',{'class':'dowload'})
            # episode_res_link = {'title':f"{tit_url}"}
            # for i in range(len(dow_url)):
            #     Url = dow_url[i].find('a')
            #     downlink = Url.get('href')
            #     str_= Url.string
            #     str_spl = str_.split()
            #     str_spl.remove(str_spl[0])
            #     str_original = ""
            #     quality_name = str_original.join(str_spl)
            #     episode_res_link.update({f"{quality_name}":f"{downlink}"})
            # episode_res_link['animeid'] = animeid; episode_res_link['episode number'] = episode_num
            # return episode_res_link
            # link = "https:" + str(soup.find_all(attrs={'rel':"100"})).split()[1][12:-1] ALL GOGO
            # link = str(soup.find_all(attrs={'rel':"14"})[0]).split()[1][12:-1] DOOD.WATCH
            # link = str(soup.find_all(attrs={'rel':"29"})[0]).split()[1][12:-1] #FEMBED
            link = str(soup.find_all(attrs={'rel':"13"})[0]).split()[1][12:-1] #streamSB
            return {"link":link}
        except AttributeError:
            return {"status":"400", "reason":"Invalid animeid or episode_num", 'animeid' : animeid, 'episode number': episode_num}
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection", 'animeid' : animeid, 'episode number': episode_num}

    def get_by_genre(genre_name, page):
        try:
            url = f"https://gogoanime.cm/genre/{genre_name}?page={page}"
            response = requests.get(url)
            plainText = response.text
            soup = BeautifulSoup(plainText, "lxml")
            animes = soup.find("ul", {"class": "items"}).find_all("li")
            gen_ani_res = [{"genre":f"{genre_name}"}]
            gen_ani = []
            for anime in animes:  # For every anime found
                tits = anime.a["title"]
                urll = anime.a["href"]
                r = urll.split('/')
                gen_ani.append({"title":f"{tits}", "animeid":f"{r[2]}"})
            gen_ani_res.append(gen_ani)
            return gen_ani_res
        except AttributeError or KeyError:
            return {"status":"400", "reason":"Invalid genre_name or page_num"}
        except requests.exceptions.ConnectionError:
            return {"status": "404", "reason": "Check the host's network Connection"}
