from django.db import models

# Create your models here.
class Catagory(models.Model):
               catagory_name=models.CharField(max_length=200,null=True)

               def __str__(self):
                       return self.catagory_name
               

class Product(models.Model):

    catagory_reference=models.ForeignKey(Catagory,null=True,on_delete=models.SET_NULL)
    product_name=models.CharField(max_length=200,null=True)
    code=models.CharField(max_length=200,null=True)
    price=models.FloatField(default=0)

    def __str__(self):

        return self.product_name