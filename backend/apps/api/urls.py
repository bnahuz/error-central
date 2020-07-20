from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^events/$', views.EventList.as_view(), name='event-list'),
    url(r'^event/(?P<pk>[0-9]+)/$', views.EventDetail.as_view(), name='event-detail'),

]