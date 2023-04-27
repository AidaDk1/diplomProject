from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from smart_selects.db_fields import ChainedForeignKey


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/category',null=True,blank=True)


    def __str__(self):
        return self.title

class SubCategory(models.Model):
    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'
    category = models.ForeignKey(Category,models.CASCADE,verbose_name='Category',)
    title = models.CharField(max_length=255)
    photo= models.ImageField( upload_to='photos/subcategory',null=True,blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True, verbose_name='категория')
    sub_category = ChainedForeignKey(
        SubCategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    name =models.CharField(max_length=50)
    description = models.CharField(max_length=65)
    price = models.PositiveIntegerField()
    product_image =models.ImageField(upload_to='photos/products/',null=True,blank=True)
    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True,blank=True,upload_to='photos/profilepics/')
    mobile = models.CharField(max_length=25,null=False)
    address = models.CharField(max_length=50)

    @property
    def __str__(self):
        return self.user.first_name
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

class Orders(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Order is Confirmed', 'Order is Confirmed'),
        ('Ready for delivery', 'Ready for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey('Customer',on_delete=models.CASCADE,null=True)
    product = models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    mobile = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    order_date = models.DateField(auto_now_add=True, null=True)

class Feedback(models.Model):
    name = models.CharField(max_length=40)
    feedback = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
