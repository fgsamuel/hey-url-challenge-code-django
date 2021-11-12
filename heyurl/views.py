from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import UrlForm
from .models import Url, Click
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

    return redirect(reverse('index'))


def short_url_view(request, short_url):
    obj = get_object_or_404(Url, short_url=short_url)

    Click.objects.create(
        url=obj,
        browser=request.user_agent.browser.family,
        platform=request.user_agent.os.family
    )

    count = Click.objects.filter(url=obj).count()
    obj.clicks = count
    obj.save()

    return redirect(obj.original_url)


def report_metrics(request, short_url):
    obj = get_object_or_404(Url, short_url=short_url)

    clicks = Click.objects.filter(url=obj)\
        .annotate(day=TruncDate('created_at'))\
        .values('day', 'browser', 'platform')\
        .annotate(total=Count('*')).order_by('-day', 'browser')

    context = dict(object=obj, clicks=clicks, object_list=clicks)
    return render(request, 'heyurl/report.html', context)
