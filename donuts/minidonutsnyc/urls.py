from django.conf.urls import url

from . import views

app_name = 'minidonutsnyc'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]