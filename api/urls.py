from django.urls import path
from .views import *

urlpatterns = [
    path('biodata',bio_list),
    # path('home',home_view),
    path('arith/',Arith)
]
