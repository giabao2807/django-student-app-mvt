from django.urls import path
from .views import detail_view, create_view

urlpatterns = [
    path('detail', detail_view, {}),
    path('create', create_view, {})
]
