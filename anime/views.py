from django.shortcuts import render
from anime.animescraping import animedealer

# Create your views here.

from django.http import HttpResponse

animes = [
    {'rank' : 1, 'name' : 'AOT'},
    {'rank' : 2, 'name' : 'Code Geass'},
    {'rank' : 3, 'name' : 'Steins;Gate'},
]

def AnimeList(request):
    # return HttpResponse('Anime List Here?')
    name = request.GET.get('name') if request.GET.get('name') != None else ''
    animes = animedealer.get_search_results(name)
    if 'status' in animes: 
        error = True
    else:
        error = False
    context = {'animes' : animes, 'error' : error}
    return render(request, 'animesearchresults.html', context)


def AnimeEpisodes(request):
    # return HttpResponse('Anime List Here?')       
    if request.GET.get('aid') != None:
        aname = request.GET.get('aid')
        (l, animename) = animedealer.get_anime_details(aname)
    else:
        l, aname, animename = (0, '', 'ERROR')
    context = {'animename': animename, 'l': list(range(1,l+1)), 'animeid': aname}
    return render(request, 'animetemplate.html', context)

def AnimeViewer(request):
    aid = request.GET.get('aid') if request.GET.get('aid') != None else ''
    epnum = request.GET.get('ep') if request.GET.get('ep') != None else 0
    episodelink = animedealer.get_episodes_link(aid, epnum)
    context = {'episodelink': episodelink, 'epnum': epnum, 'aid': aid}
    return render(request, 'animeviewer.html', context)