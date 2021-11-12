from django.urls import path

from heyurl import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store', views.store, name='store'),
    path('report/<str:short_url>/', views.report_metrics, name='report_metrics'),
]
