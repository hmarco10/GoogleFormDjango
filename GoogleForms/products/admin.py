from django.contrib import admin
from .models import Product


# admin.site.register(Product)
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    #list_display = ('name', 'category', 'description', 'price',)
    list_display = ('User','titulo', 'descripcion','pregunta',)
    list_filter = ('id',)
















"""
@admin.register(Question)
class AdminQuestio(admin.ModelAdmin):
    #list_display = ('name', 'category', 'description', 'price',)
    list_display = ('TitleForm', 'question',)
    list_filter = ('id',)

@admin.register(Answer)
class AdminAnswer(admin.ModelAdmin):
    #list_display = ('name', 'category', 'description', 'price',)
    list_display = ('formQuestion', 'answer',)
    list_filter = ('id',)


@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
    list_display = ('user', 'product',)
    list_filter = ('user', 'product',)
"""