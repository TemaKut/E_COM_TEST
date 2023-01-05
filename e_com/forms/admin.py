from django.contrib import admin

from .models import Form


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    """ Регистрация в админке и приведение к надлежащему виду. """
    list_display = [
        'name',
        'date',
        'email',
        'phone',
        'text',
    ]
    search_fields = [
        'name',
        'email',
        'phone',
    ]
    list_filter = [
        'name',
        'date',
        'email',
        'phone',
    ]
