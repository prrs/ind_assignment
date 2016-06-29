from __future__ import unicode_literals

from django.db import models

class Resource(models.Model):
    def __str__(self):
        return self.number + ", " + self.volume + ", " + str(self.page)
    number = models.CharField(max_length=10, unique=True)
    volume = models.CharField(max_length=10)
    page = models.PositiveIntegerField()

class Image(models.Model):
    def __str__(self):
        return self.img
    img = models.CharField(max_length=50)
    resource = models.ForeignKey('Resource')
