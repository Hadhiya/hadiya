from django.contrib import admin

# Register your models here.
from.models import Admin
from.models import UserRegistration
from.models import Item

admin.site.register(Admin)
admin.site.register(UserRegistration)
admin.site.register(Item)