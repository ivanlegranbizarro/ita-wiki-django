from django.db import models

from users_dni.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categorías'
        verbose_name = 'Categoría'

        ordering = ['title']

    def __str__(self):
        return f'{self.title}'


class Tema(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(
        Category, related_name='tema_categories')


class Wiki(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='student_wikis')
    url = models.URLField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category_wikis')
    tema = models.ForeignKey(
        Tema, on_delete=models.PROTECT, related_name='tema_wikis')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Recursos'
        verbose_name = 'Recurso'

        ordering = ['title']

    def __str__(self):
        return f'{self.title} - {self.student}'
