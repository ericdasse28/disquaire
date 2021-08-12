from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from .forms import ContactForm
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
    album = get_object_or_404(Album, pk=album_id)
    artists = [artist.name for artist in album.artists.all()]
    artists_name = " ".join(artists)

    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture,
    }

    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')

        contact = Contact.objects.filter(email=email)
        if not contact.exists():
            # If a contact is not registered, create a new one.
            contact = Contact.objects.create(
                email=email,
                name=name
            )

        # If no album matches the id, it means the form must have been tweaked
        # so returning a 404 is the best solution
        album = get_object_or_404(Album, id=album_id)
        booking = Booking.objects.create(
            contact=contact,
            album=album
        )

        # Make sure no one can book the album again
        album.available = False
        album.save()
        context = {
            'album_title': album.title
        }

        return render(request, 'store/merci.html', context)
    else:
        # GET method. Create a new form to be used in the template
        form = ContactForm()

    context['form'] = form

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
