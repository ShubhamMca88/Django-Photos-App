from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^search/", views.search, name="search_results"),
    url(r"^browse/$", views.browse, name="browse"),
    url(r"^location/(\d+)", views.location_filter, name="location"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)