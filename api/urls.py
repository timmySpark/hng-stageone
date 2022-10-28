from django.urls import path
from .views import *

urlpatterns = [
    path('biodata',bio_list)
]
