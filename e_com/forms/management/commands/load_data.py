import csv

from django.conf import settings
from django.core.management import BaseCommand

from forms.models import Form


class Command(BaseCommand):
    """ Загрузка тестовых данных в модель Form. """

    def handle(self, *args, **options):

        with open(
            f'{settings.BASE_DIR}/test_data.csv',
            'r', encoding='utf-8',
        ) as table:

            reader = csv.DictReader(table)
            Form.objects.bulk_create(
                Form(**data) for data in reader
            )

        self.stdout.write(self.style.SUCCESS('==-- Загружено! --=='))
