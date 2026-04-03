from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    mob = models.CharField('mobile', max_length=50)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name
