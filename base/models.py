from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    arabian_product = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    



