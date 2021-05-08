from django.contrib import admin
from django.forms import ModelForm

from .models import SubCategory, Category, Seed, SeedPhotos, Manufacturer
# Register your models here.


admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Seed)
admin.site.register(SeedPhotos)
admin.site.register(Manufacturer)
