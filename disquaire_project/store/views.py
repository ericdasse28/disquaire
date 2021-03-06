from django.http import HttpResponse
# from .models import ALBUMS


def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)


def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))

    return HttpResponse(message)


def detail(request, album_id):
    a_id = int(album_id)  # Make sure we have an integer
    album = ALBUMS[a_id]  # Get the album with its id
    artists = " ".join([artist['name'] for artist in album['artists']])  # Grab artists name and
    # create a string out of it.
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)

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
