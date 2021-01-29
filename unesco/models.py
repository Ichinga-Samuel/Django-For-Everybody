from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Iso(models.Model):

    name = models.SlugField()

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True)
    justification = models.CharField(max_length=250, null=True)
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
