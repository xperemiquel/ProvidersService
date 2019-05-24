from django.db import models
from django.core.validators import RegexValidator
# from django.contrib.gis.db import models as geomodels
from djgeojson.fields import PointField

class Provider(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Please, enter the phone number in a correct format.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class ServiceArea(models.Model):
    name = models.CharField(max_length=10)
    polygon = PointField(blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.name