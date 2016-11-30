from django.conf.urls import url
from users import views
from matches import views

urlpatterns = [
    url(r'^create/$', views.create_match, name='create_match'),
    url(r'^get/$', views.get_match, name='get_match'),
    url(r'^(?P<match_id>[0-9]+)/get_match/$', views.get_match, name='get_match'),
]
