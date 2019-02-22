from django.http import HttpResponse
from .models import Album
from django.shortcuts import render, get_object_or_404
from django.http import Http404


# from django.template import loader

def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('')
    # context = {
    #     'all_album': all_albums,
    # }
    return render(request, 'music/index.html', {'all_album': all_albums})
    # html = ''
    # for album in all_album:
    #     url='/music/' + str(album_id) + '/'
    #     html += '<a href = "' + url + '">'> + album.album_title + '</a><br>'
    # return HttpResponse(template.render(context,request))


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    # return HttpResponse("<h2>Details for Album id:" + str(album_id) + "</h2>")
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exit")
    return render(request, 'music/detail.html', {'album': album})
