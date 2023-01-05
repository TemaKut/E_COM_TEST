from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import FormSerializer
from forms.models import Form


@api_view(['POST'])
def add_forms(request):
    """ Добавление списка форм в БД с дальнейшей валидацией. """
    serializer = FormSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def get_form(request):
    """
    При POST запросе и соответствующих параметрах запроса отдаёт имя формы.
    В случае отсутствия формы в БД отдаёт поля и должными типами.
    """
    query_params = request.query_params.dict()
    fields = [field.name for field in Form._meta.get_fields()]

    search_fields = {
        key: value for key, value in query_params.items() if key in fields
    }

    form = Form.objects.filter(**search_fields).first()


    if form and search_fields:

        return Response(form.name, status=status.HTTP_200_OK)

    return Response(
        {
            'name': 'Любой набор символов.',
            'date': 'Формат даты: 2000-08-29',
            'phone': 'Формат номера: +7 xxx xxx xx xx',
            'email': 'Формат email@mail.ru',
            'text': 'Любой набор символов.',
        },
        status=status.HTTP_404_NOT_FOUND,
    )
