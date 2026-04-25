from django.urls import path
from .views import optimize_route, home

urlpatterns = [
    path('', home),            # http://127.0.0.1:8000/
    path('route/', optimize_route),  # http://127.0.0.1:8000/route/
]