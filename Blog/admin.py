from django.contrib import admin

from .models import Category, Tag, Post

'''
Class field prepopulated fields is required for automatic filling in of the slug.
For this action use models fields (For example 'title')
'''


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Category)
# admin.site.register(Post)
# admin.site.register(Tag)
