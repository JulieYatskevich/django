from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views


urlpatterns = [
   path('', views.index),
   path('main', views.index, name="main")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
