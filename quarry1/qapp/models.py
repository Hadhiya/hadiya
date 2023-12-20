from django.db import models

# Create your models here.

class Admin(models.Model):
    id = models.IntegerField(primary_key=True)
    admin_id = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.admin_id


class UserRegistration(models.Model):
    u_name = models.CharField(max_length=50)
    u_address = models.CharField(max_length=150)
    u_place = models.CharField(max_length=100)
    u_contact = models.IntegerField()
    u_email = models.TextField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.u_name


class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True,default=0)
    cat_name = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_name


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_quantity = models.IntegerField()
    item_price = models.IntegerField()
    item_img=models.FileField()

    def __str__(self):
        return self.item_name


class Cart(models.Model):
    cart_amount = models.IntegerField()
    item_id = models.IntegerField(default=0)
    username = models.CharField(max_length=50, default="default_username")

    def __str__(self):
        return self.cart_amount


class OrderMaster(models.Model):
    username = models.CharField(max_length=50)
    odate = models.IntegerField()
    grand_total = models.IntegerField()
    u_address = models.CharField(max_length=150)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.odate


class OrderItem(models.Model):
    order_mas_id = models.IntegerField()
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return self.quantity
