from django.urls import path
from .views import create_event, get_event_detail, get_archieve

urlpatterns = [
    path('', create_event, name = "create_event"),
    path('<int:id>', get_event_detail, name = "get_event_detail"),
    path('<int:year>/<int:month>', get_archieve, name = "get_archieve")
]