from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    User = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250, default="")
    descripcion = models.CharField(max_length=255, default="")
    pregunta = models.CharField(max_length=255, default="")

    def __str__(self):
        return str(self.titulo) 
    class Meta:
        ordering = ('id',)

"""
class Question(models.Model):
    TitleForm = models.ForeignKey(Product, on_delete=models.CASCADE)
    question=models.CharField(max_length=250)
    

    def __str__(self):
        return self.question

    class Meta:
        ordering = ('id',)


class Answer(models.Model):
    formQuestion = models.ForeignKey(Question, default="", blank=False, on_delete=models.CASCADE)
    answer=models.CharField(max_length=250)
    

    def __str__(self):
        return self.answer

    class Meta:
        ordering = ('id',)

"""




"""
class Favorite(models.Model):
    user = models.ForeignKey(Client)
    product = models.ForeignKey(Product)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return '%s %s' % (self.user.name, self.product.name)
"""