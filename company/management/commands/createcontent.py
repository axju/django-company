from django.core.management.base import BaseCommand, CommandError
from company.models import Portfolio, Post
import random
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    default_title = ['Title', 'Title B', 'Title C']
    default_description = ['Bla bla bla bla abl balb alb lablkdflwev sd fsv cvx']
    default_text = ['Bla bla bla bla abl balb alb lablkdflwev sd fsv cvx']


    def create_portfolio(self, n, category):
        for i in range(n):
            info=None
            title=random.choice(self.default_title)
            description=random.choice(self.default_description)
            text=random.choice(self.default_text)

            if category == 'feature': info = Post.objects.create(title=title, text=text)
            Portfolio.objects.create(title=title, category=category, description=description, info=info)

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        Portfolio.objects.all().delete()
        self.create_portfolio(4, 'headline')
        self.create_portfolio(6, 'feature')

        self.stdout.write(self.style.SUCCESS('Successfully create content'))
