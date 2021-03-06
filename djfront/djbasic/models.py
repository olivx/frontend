from django.db import models


class Customer(models.Model):
    name = models.CharField('nome', max_length=50)
    email = models.EmailField()

    class Meta:
        ordering = ['name']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField('nome', max_length=50)
    age = models.IntegerField('idade', null=True, blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'

    def __str__(self):
        return self.name
