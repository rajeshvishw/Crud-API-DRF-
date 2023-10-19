from django.db import models

class webModel(models.Model):
    product_name = models.CharField(max_length=50,null = True,blank=True)
    Product_price = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    product_image = models.ImageField()
