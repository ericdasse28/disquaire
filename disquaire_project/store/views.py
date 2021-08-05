from django.http import HttpResponse
from django.template import loader
from .models import Album, Artist, Contact, Booking


def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    # message = """<ul>{}</ul>""".format("\n".join(formatted_albums))

    context = {
        'albums': albums
    }

    template = loader.get_template('store/index.html')
    return HttpResponse(template.render(context, request=request))


def listing(request):
    albums = Album.objects.filter(available=True)
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}<ul>""".format("\n".join(formatted_albums))

    return HttpResponse(message)


def detail(request, album_id):
    a_id = int(album_id)  # Make sure we have an integer
    album = Album.objects.get(pk=album_id)  # Get the album with its id
    artists = " ".join([artist.name for artist in album.artists.all()])  # Grab artists name and
    # create a string out of it.
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)

    return HttpResponse(message)


def search(request):
    query = request.GET.get('query')

    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)

        if not albums.exists():
            albums = Album.objects.filter(artists__name__icontains=query)

        if not albums.exists():
            message = "Misère de misère ! Nous n'avons trouvé aucun résultat"
        else:
            albums = ["<li>{}</li>".format(album.title) for album in albums]
            message = """
                Nous avons trouvé les albums correspondant à votre requête ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("\n".join(albums))

    return HttpResponse(message)
