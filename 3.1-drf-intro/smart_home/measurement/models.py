from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=120, verbose_name='Датчик')
    description = models.CharField(max_length=150, verbose_name='Место расположения')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    sensors = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
