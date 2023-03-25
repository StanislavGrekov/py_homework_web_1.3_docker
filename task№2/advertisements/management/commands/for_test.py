from django.core.management.base import BaseCommand
from advertisements.models import Advertisement
from django.contrib.auth.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):

        User.objects.create(username='user', password = '123456', is_staff= True)
        Advertisement.objects.create(title="Продам холодильник", description="Очень хороший холодильник",
                                    status='Open', creator_id=1, open='True')


        pass