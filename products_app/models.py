from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=40)
    product_price = models.IntegerField(unique=True)
    product_info = models.CharField(max_length=255)
    sklad = models.BooleanField(default=False)
    product_size = models.IntegerField(unique=True)
    creat_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name