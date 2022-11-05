from django.urls import path
from .views import *

urlpatterns = [
    path('biodata',bio_list),
    path('eval/',solve),
    path('solve/',SolveApiView.as_view())
]
