""" URL routes for Tracks API views """
from django.conf.urls import url

from .views import TrackListAPI, TrackDetailAPI, TrackUploadAPI


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', TrackDetailAPI.as_view(), name='track-detail'),
    url(r'^', TrackListAPI.as_view(), name='track-list'),
    url(r'^upload', TrackUploadAPI.as_view(), name='track-upload')
]
