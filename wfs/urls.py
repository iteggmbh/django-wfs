from django.urls import re_path
from wfs.views import global_handler,related_handler

# APP
urlpatterns = [
    re_path(r'^(?P<service_id>\d+)/$',global_handler, name='wfs'),
    re_path(r'^(?P<service_id>\d+)/related/$',related_handler, name='wfs-related'),
]
