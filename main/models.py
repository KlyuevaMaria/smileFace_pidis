from django.db import models

class Facility(models.Model):
    photo = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    desc = models.TextField(default="описание")

    def __str__(self):
        return self.name


class Photographers(models.Model):
    name = models.CharField(max_length=100, blank=False)
    service = models.ForeignKey(Facility, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=60, blank=False)
    phone = models.IntegerField()


class Gallery(models.Model):
    photo = models.ImageField(upload_to='products/')
    desc = models.TextField(default="описание")