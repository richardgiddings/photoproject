from django.contrib import admin
from imagekit.admin import AdminThumbnail
from .models import Photo, Category

admin.site.register(Photo)
admin.site.register(Category)