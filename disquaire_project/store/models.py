from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)
