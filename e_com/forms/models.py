from django.db import models


class Form(models.Model):
    """ Модель формы. """

    name = models.CharField(
        verbose_name='Имя формы',
        max_length=50,
        null=False,
    )
    date = models.DateField(
        verbose_name='Дата',
        null=False,
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=20,
        unique=True,
        null=False,
    )
    email = models.EmailField(
        verbose_name='Почта',
        unique=True,
        null=False,
    )
    text = models.TextField(
        verbose_name='Текст',
        max_length=500,
        null=False,
    )

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'

    def __str__(self):
        """ Строчное представление. """

        return self.name
