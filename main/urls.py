from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path("read/", views.read_page, name='reader'),
    path("filter", views.homepage, name='filter'),
    path("", views.homepage, name='homepage'),
]
