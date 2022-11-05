from django.urls import path
from .views import *

urlpatterns = [
    path('biodata',bio_list),
    path('eval/',solve_list),
    path('solve/',SolveApiView.as_view())
]
