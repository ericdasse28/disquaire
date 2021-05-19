from django.db import models

ARTISTS = {
    'francis-cabrel': {'name': 'Francis Cabrel'},
    'lej': {'name': 'Elijay'},
    'rosana': {'name': 'Rosanna'},
    'maria-dolores-pradera': {'name': 'Maria Dolores Pradera'},
}

ALBUMS = [
    {'name': 'Sarcabane', 'artists': [ARTISTS['francis-cabrel']]},
    {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
    {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]
