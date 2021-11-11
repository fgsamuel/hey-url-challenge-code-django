from django.urls import reverse

from heyurl.models import Url


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
