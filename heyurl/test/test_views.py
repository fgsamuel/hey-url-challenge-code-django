from django.urls import reverse

from heyurl.models import Url, Click


def test_post_original_url(client, db):
    url = reverse('store')
    data = dict(original_url='http://google.com')
    client.post(url, data=data)
    assert Url.objects.all().count() == 1


def test_error_message_duplicated(client, db):
    Url.objects.create(original_url='http://google.com', short_url='12345')
    url = reverse('store')
    data = dict(original_url='http://google.com')
    client.post(url, data=data)
    assert Url.objects.all().count() == 1


def test_message_error_form(client, db):
    Url.objects.create(original_url='http://google.com', short_url='12345')
    url = reverse('store')
    data = dict(original_url='http://google.com')
    resp = client.post(url, data=data)
    assert 'Original url already exists' in str(resp.content)


def test_post_create_metrics_class(client, db):
    Url.objects.create(original_url='http://google.com', short_url='12345')
    url = reverse('short_url', kwargs={'short_url': '12345'})
    client.get(url)
    assert Click.objects.all().count() == 1


def test_post_create_metrics_field(client, db):
    obj = Url.objects.create(original_url='http://google.com', short_url='12345')
    url = reverse('short_url', kwargs={'short_url': '12345'})
    client.get(url)
    obj.refresh_from_db()
    assert obj.clicks == 1


def test_short_url_404(client, db):
    url = reverse('short_url', kwargs={'short_url': '12345'})
    resp = client.get(url)
    assert resp.status_code == 404
