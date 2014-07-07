from feed.models import Source, Item
from datetime import datetime
import pytz
import feedparser

def update_feeds():
    sources = Source.objects.all()
    for source in sources:
        feed = feedparser.parse(source.url)
        new_entries = [entry for entry in feed.entries if (pytz.utc.localize(datetime(*(entry.published_parsed[0:6]))) > source.updated)]
        for entry in new_entries:
            item = Item(source = source, url = entry.link)
            item.save()
