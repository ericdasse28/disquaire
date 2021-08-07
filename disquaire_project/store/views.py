from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Album, Artist, Contact, Booking


def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    # message = """<ul>{}</ul>""".format("\n".join(formatted_albums))

    context = {
        'albums': albums
    }

    return render(request, 'store/index.html', context)


def listing(request):
    albums_list = Album.objects.filter(available=True)
    paginator = Paginator(albums_list, 9)
    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)

    context = {
        'albums': albums,
        'paginate': True
    }

    return render(request, 'store/listing.html', context)


def detail(request, album_id):
    a_id = int(album_id)  # Make sure we have an integer
    album = get_object_or_404(Album, pk=a_id)  # Get the album with its id
    artists = " ".join([artist.name for artist in album.artists.all()])  # Grab artists name and
    artists_name = " ".join(artists)
    # create a string out of it.
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)

    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }

    return render(request, 'store/detail.html', context)


def search(request):
    query = request.GET.get('query')

    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)

        if not albums.exists():
            albums = Album.objects.filter(artists__name__icontains=query)

    title = f"Résultats pour la requête {query}"
    context = {
        'albums': albums,
        'title': title
    }

    return render(request, 'store/search.html', context)
