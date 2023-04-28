from django.urls import path, include
from .views import courses_view
from . import api_urls

urlpatterns = [
    path('', courses_view),
    path('api/', include(api_urls))
]

