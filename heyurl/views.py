from django.shortcuts import render
from django.http import HttpResponse

from .forms import UrlForm
from .models import Url
from .services import create_short_url


def index(request):
    urls = Url.objects.order_by('-created_at')
    form = UrlForm()
    context = {'urls': urls, 'form': form}
    return render(request, 'heyurl/index.html', context)


def store(request):
    if request.method == 'POST':
        urls = Url.objects.order_by('-created_at')
        form = UrlForm(request.POST)
        if not form.is_valid():
            context = {'urls': urls, 'form': form}
            return render(request, 'heyurl/index.html', context)
        obj = form.save(commit=False)
        obj.short_url = create_short_url()
        obj.save()

    return HttpResponse("Storing a new URL object into storage")

def short_url(request, short_url):
    # FIXME: Do the logging to the db of the click with the user agent and browser
    return HttpResponse("You're looking at url %s" % short_url)
