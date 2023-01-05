from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from forms.models import Form


class TestForms(APITestCase):
    """ Тестирование работоспособности forms. """

    def setUp(self):
        """ Выполнение над каждым тестовым случаем. """
        self.client = APIClient()

        self.add_forms = reverse('api:add_forms')
        self.get_form = reverse('api:get_form')

        self.test_form = Form.objects.create(
            name='17_Название1',
            date='2000-08-29',
            phone='+7 310 101 19 27',
            email='1artem@mail.ru',
            text='Текст1',
        )

    def test_add_form(self):
        """ Тестирование добавление формы через API. """
        count_forms_before = Form.objects.all().count()

        test_data = {
            'name': '1_Название',
            'date': '2000-08-29',
            'phone': '+7 300 101 19 27',
            'email': '1atem@mail.ru',
            'text': 'Текс1',
        }

        response = self.client.post(self.add_forms, data=test_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        count_forms_after = Form.objects.all().count()
        self.assertEqual(count_forms_before, count_forms_after - 1)

    def test_get_form(self):
        """
        Тестирование получения названия формы после POST запроса с нужными,
        а так же лишними параметрами.
        """
        response = self.client.post(
            f'{self.get_form}?name=17_Название1&text=Текст1&soooome=test',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.test_form.name)

    def test_error_msg_get_form(self):
        """
        Тестирование сообщения об ошибке
        при передаче всех неправильных параметров в get_form.
        """
        response = self.client.post(
            f'{self.get_form}?&soooome=test',
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(
            response.data,
            {
                'name': 'Любой набор символов.',
                'date': 'Формат даты: 2000-08-29',
                'phone': 'Формат номера: +7 xxx xxx xx xx',
                'email': 'Формат email@mail.ru',
                'text': 'Любой набор символов.',
            }
        )
