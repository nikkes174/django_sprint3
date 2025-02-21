from django.contrib import admin
from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_editable = (
        'title',
        'description',
        'slug',
    )


class LocationAdmin(admin.ModelAdmin):
    list_editable = (
        'name'
    )


class PostAdmin(admin.ModelAdmin):
    list_editable = (
        'title',
        'Текст'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
