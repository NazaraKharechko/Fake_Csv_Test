import os

from django.db import models
from django.core.validators import RegexValidator


class DataModel(models.Model):
    class Meta:
        db_table = 'company'
        verbose_name = 'компанії'
        verbose_name_plural = 'компанія'

    ful_name = models.CharField(max_length=50)
    job = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True,
                             validators=[RegexValidator('^([0])(\d{9})$', 'not valid phone number')])
    description = models.CharField(max_length=500, default='', blank=True)
    date = models.DateField()
    photo = models.ImageField(upload_to=os.path.join('face', 'img'), default='', blank=True)

    def __str__(self):
        return self.ful_name
