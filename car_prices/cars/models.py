from django.db import models

# Create your models here.


class VehicleType(models.Model):
    name = models.CharField(max_length=50)
    value = models.PositiveSmallIntegerField(
        unique=True, primary_key=True, editable=True)

    def __str__(self):
        return '{} ({})'.format(self.name, self.value)


class Make(models.Model):
    vehicle_type = models.ForeignKey(
        'VehicleType', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.PositiveSmallIntegerField(
        unique=True, primary_key=True, editable=False)

    def __str__(self):
        return '{} ({})'.format(self.name, self.value)


class Model(models.Model):
    make_type = models.ForeignKey(
        'Make', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.PositiveSmallIntegerField(
        unique=True, primary_key=True, editable=False)

    def __str__(self):
        return '{} ({})'.format(self.name, self.value)
