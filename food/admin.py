from django.contrib import admin

from .models import Food, FoodCategory


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('category', 'is_vegan', 'is_special', 'code', 'internal_code', 'name_ru',
                    'description_ru', 'description_en', 'description_ch', 'cost', 'is_publish')


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en', 'name_ch', 'order_id')

