from django.db import models

# Create your models here.

class Ingredients(models.Model):
    """Ingredients model"""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Ingredients, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.name)

class Recipes(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    steps = models.TextField(blank=False)
    ingredients = models.ManyToManyField(Ingredients)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)