from django.core.management.base import BaseCommand, CommandError
from feed.functions import update_feeds

class Command(BaseCommand):
    help = 'Updates rss feeds'

    def handle(self, *args, **options):
        update_feeds()
