from django.http import HttpResponse
from .models import Album, Artist, Contact, Booking


def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    return HttpResponse(message)


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
        message = "Aucun artiste n'est demandé"
    else:
        albums = [
            album for album in ALBUMS
            if query in " ".join(artist['name'] for artist in album['artists'])
        ]

        if len(albums) == 0:
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
            message = """
                Nous avons trouvé les albums correspondant à votre requête ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("\n".join(albums))

    return HttpResponse(message)
