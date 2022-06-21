from django.db import models

# Create your models here.

class TitleScreens(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=800)


class Sposoby(models.Model):
    nazwaSposobu = models.CharField(max_length=255)
    opisSposobu = models.TextField(max_length=3000)
    
    def __str__(self):
        return self.nazwaSposobu
    


class Napisz(models.Model):
    tytul = models.CharField(max_length=255)
    wykonanie = models.TextField(max_length=3000)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.tytul
    