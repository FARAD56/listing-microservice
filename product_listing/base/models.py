from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) -> str: 
        return str(self.id)+' : '+str(self.name)
    
class Region(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) -> str: 
        return str(self.id)+' : '+str(self.name)
    

class Shop(models.Model):
    name=models.CharField(max_length=100)
    user_id=models.IntegerField(default=0)
    location=models.CharField(max_length=10000)

    def __str__(self) -> str: 
        return str(self.id)+' : '+str(self.name)


class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    shop_id=models.ForeignKey(Shop, on_delete=models.CASCADE,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=11,default=0)
    stock_quantity=models.IntegerField(default=0)
    category_id= models.ForeignKey(Category, on_delete=models.CASCADE)
    region_id= models.ForeignKey(Region, on_delete=models.CASCADE)
    image=models.CharField(max_length=10000,default='https://img.freepik.com/free-vector/shopping-cart-realistic_1284-6011.jpg?size=338&ext=jpg&ga=GA1.1.1141335507.1718064000&semt=ais_user')

    def __str__(self) -> str:
        return str(self.id)+' : '+str(self.name)
    

