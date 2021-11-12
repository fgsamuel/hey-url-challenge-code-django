from django.urls import path

from heyurl import views

urlpatterns = [
    path('', views.short_url_view, name='short_url'),
]
