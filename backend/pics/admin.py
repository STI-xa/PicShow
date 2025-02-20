from django.contrib import admin
from .models import Photo, Tag 

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('author', 'description', 'pub_date', 'image', 'tag')
    list_filter = ('author', 'tag',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
