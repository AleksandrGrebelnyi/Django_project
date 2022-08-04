from django.db import models


class Categories(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position')


class Dish(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    description = models.TextField('Description')
    position = models.SmallIntegerField(unique=True)
    price = models.FloatField('Price')
    photo = models.ImageField(width_field=50, height_field=50)
    specialty = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position')


class Events(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    description = models.TextField('Description')
    price = models.FloatField('Price')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name')


class Gallery(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    photo = models.ImageField(width_field=50, height_field=50)

    def __str__(self):
        return f'{self.name}'
