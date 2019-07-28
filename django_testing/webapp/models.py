from django.db import models

class Product(models.Model):
    name         = models.CharField(max_length=128)
    price        = models.DecimalField(max_digits=5, decimal_places=2)
    quantity     = models.IntegerField()
    description  = model.TextField()
    published_on = models.DateField()

    @property
    def is_in_stock(self):
        return self.quantity > 0
