import feedparser
import datetime
import urllib2

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from feed.models import Item, Source

def display(request):
    if request.user.is_authenticated():
        if request.GET.has_key('read'):
            item = Item.objects.order_by('-last_read').first()
            item.delete()
        item = Item.objects.filter(source__owner = request.user.pk).order_by("?").first()
        if not item:
            return HttpResponseRedirect(reverse('feed:add_source'))
        else:
            item.skipped += 1
            item.last_read = datetime.datetime.now()
            item.save()
            return HttpResponseRedirect(item.url)
    else:
        return HttpResponseRedirect(reverse('archives:index'))

def add_source(request):
    if request.user.is_authenticated():
        if request.META['REQUEST_METHOD'] == 'GET':
            return render(request, 'feed/add_source.html', {})
        else:
            url = urllib2.unquote(request.POST['url']).decode("utf8")
            feed = feedparser.parse(url)
            source = Source(owner=request.user, name = feed.feed.title, url = request.POST['url'])
            source.save()
            for i in range(0,9):
                item = Item(source = source, url = feed.entries[i].link)
                item.save()
            return HttpResponseRedirect(reverse('feed:add_source')) 
    else:
        return HttpResponseRedirect(reverse('archives:index'))


