'''
Models that use in project.

    Category
===============
title, slug, smart_icon

    Tag
============
title, slug

    Post
============
title, slug, content, created_at, photo, views, category, tags
'''

from django.db import models


class Category(models.Model):
    """
    ==========
        title: VARCHAR(255)
        slug: VARCHAR(255), unique=True
        smart icon: VARCHAR(255) for save path to image file
    ==========
    """
    title = models.CharField(max_length=255, verbose_name='Наименование категории')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    smart_icon = models.ImageField(verbose_name='Миниатюра категории', upload_to='CategoryIcon')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    """
    ==========
        title: VARCHAR(255)
        slug: VARCHAR(50), unique=True
    ==========
    """
    title = models.CharField(max_length=255, verbose_name='Наименование категории')
    slug = models.SlugField(max_length=50, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']


class Post(models.Model):
    """
    ==========
        title: VARCHAR(255)
        slug: VARCHAR(255), unique=True
        content: TEXT, null=True
        created at: DATE
        photo: VARCHAR(255) for save file path
        views: INTEGER, default 0
        category: FOREIGNKEY CATEGORY, on delete PROTECT, related_name is posts (related name could use when i want refer to the linked model)
        tags: FOREIGNKEY TAG but n->n, null=True, related name is posts
    ==========
    """
    title = models.CharField(max_length=255, verbose_name='Тема поста')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Миниатюра для поста', blank=True)
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория поста',
                                 related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Тэг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
