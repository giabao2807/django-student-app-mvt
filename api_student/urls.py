from django.urls import path
from .views import detail_view, create_view, update_view, list_view, delete_view

urlpatterns = [
    path('<int:id>/delete', delete_view, name='delete'),
    path('<int:id>/update', update_view, name='update'),
    path('<int:id>/detail', detail_view, name='detail'),
    path('create', create_view, name='create'),
    path('', list_view, name='students')
]
