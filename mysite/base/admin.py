from django.contrib import admin
from .models import Categories, Dish, Events, Gallery, About, Specials, WhyUs, UserReservation, Contact

# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', ), }


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ('category', 'price', )
    prepopulated_fields = {'slug': ('name', ), }


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    prepopulated_fields = {'slug': ('name', ), }


admin.site.register(Gallery)
admin.site.register(About)
admin.site.register(WhyUs)
admin.site.register(Specials)
admin.site.register(UserReservation)
admin.site.register(Contact)

