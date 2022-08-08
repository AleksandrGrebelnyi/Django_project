from django.db import models
import uuid  # задаем новое уникальное имя файлу
import os

class Categories(models.Model):
    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', )
        index_together = (('id', 'slug'), )


class Dish(models.Model):

    def get_file_name_dish(self, filename: str) -> str:
        end_file_name = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{end_file_name}'
        return os.path.join('dishes/', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    description = models.TextField(max_length=500, blank=True)  #blank True can be empty
    position = models.SmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name_dish)
    specialty = models.BooleanField(default=False)
    ingredients = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', 'price', )
        index_together = (('id', 'slug'), )


class Events(models.Model):

    def get_file_name_events(self, filename: str) -> str:
        end_file_name = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{end_file_name}'
        return os.path.join('events/', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name_events)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'), )


class Gallery(models.Model):

    def get_file_name_gallery(self, filename: str) -> str:
        end_file_name = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{end_file_name}'
        return os.path.join('gallery/', new_filename)

    photo = models.ImageField(upload_to=get_file_name_gallery)


class About(models.Model):
    info_about_us = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.info_about_us}'


class WhyUs(models.Model):
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.description}'


class Specials(models.Model):

    def get_file_name_specials(self, filename: str) -> str:
        end_file_name = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{end_file_name}'
        return os.path.join('dishes/', new_filename)

    name = models.CharField(unique=True, max_length=50, db_index=True)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to=get_file_name_specials)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
