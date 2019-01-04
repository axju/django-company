from django.core.management.base import BaseCommand, CommandError
from company.models import Feature
import random

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for i in range(10):
            Feature.objects.create(
                title='title '+str(i),
                description='Bla bla bla bla abl balb alb lablkdflwev sd fsv cvx',
                text='Bla bla bla bla abl balb alb lablkdflwev sd fsv cvx',)

        self.stdout.write(self.style.SUCCESS('Successfully create content'))
