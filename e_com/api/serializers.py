import re

from rest_framework import serializers

from forms.models import Form


class FormSerializer(serializers.ModelSerializer):
    """ Сериализация форм. """

    class Meta:
        model = Form
        fields = '__all__'

    def validate_phone(self, value):
        """ Валидация поля phone. """

        search_result = re.search(
            r'\+7 (\d){3} (\d){3} (\d){2} (\d){2}',
            value,
        )

        if search_result:

            return search_result.group(0)

        raise serializers.ValidationError('Формат номера: +7 xxx xxx xx xx')
