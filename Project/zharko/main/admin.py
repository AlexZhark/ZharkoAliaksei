from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Catalog)
admin.site.register(models.Review)