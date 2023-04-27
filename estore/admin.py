from django.contrib import admin

# Register your models here.
from estore.models import Category, SubCategory, Product, Customer, Orders, Feedback

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Feedback)
