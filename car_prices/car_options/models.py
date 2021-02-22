from django.db import models

# Create your models here.


class Transmission(models.Model):
    name = models.CharField(max_length=50)
    value = models.PositiveSmallIntegerField(
        unique=True, primary_key=True, editable=False)

    def __str__(self):
        return '{} ({})'.format(self.name, self.value)
