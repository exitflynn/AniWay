from django.shortcuts import render
from anime.animescraping import animedealer

# Create your views here.

from django.http import HttpResponse

def AnimeList(request):
    name = request.GET.get('name') if request.GET.get('name') != None else ''
    animes = animedealer.get_search_results(name)
    if 'status' in animes: 
        error = True
    else:
        error = False
    context = {'animes' : animes, 'error' : error, 'coins':getCoins()}
    return render(request, 'animesearchresults.html', context)


def AnimeEpisodes(request):
    # return HttpResponse('Anime List Here?')       
    if request.GET.get('aid') != None:
        aname = request.GET.get('aid')
        (l, animename, img) = animedealer.get_anime_details(aname)
    else:
        l, aname, animename, img = (0, '', 'ERROR', '')
    coins = getCoins()
    context = {'animename': animename, 'l': list(range(1,l+1)), 'animeid': aname, 'coins':coins, 'img' : img}
    return render(request, 'animetemplate.html', context)

def AnimeViewer(request):
    aid = request.GET.get('aid') if request.GET.get('aid') != None else ''
    epnum = request.GET.get('ep') if request.GET.get('ep') != None else 0
    episodelink = animedealer.get_episodes_link(aid, epnum)
    
    b = int(open('anime/coinsSpent.txt', 'r').read())
    b+=1
    c = open('anime/coinsSpent.txt', 'w')
    c.write(str(b)); c.close()
    coins = getCoins()
    if coins <= 0:
        # return HttpResponse('You Broke.')
        return render(request, 'goback.html')
    else:
        context = {'episodelink': episodelink, 'epnum': epnum, 'aid': aid, 'coins' : coins}
        return render(request, 'animeviewer.html', context)
def getCoins():
    a = open('anime/tokensEarned.txt', 'r')
    b = open('anime/coinsSpent.txt', 'r')
    tokensEarned = int(a.read())
    coinsSpent = int(b.read())
    coins = tokensEarned-coinsSpent
    a.close(); b.close()
    return coins
