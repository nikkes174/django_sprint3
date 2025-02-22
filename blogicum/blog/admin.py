from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name')


@admin.register(Category)
class CategoryPostAdmin(admin.ModelAdmin):
    list_display = ('title')
