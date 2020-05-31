from django.urls import path
from .views import list_agenda, create_agenda, update_agenda, delete_agenda

urlpatterns = [
    path('', list_agenda, name='list_agenda'),
    path('new', create_agenda, name='create_agenda'),
    path('update/<int:id>/', update_agenda, name='update_agenda'),
    path('delete/<int:id>/', delete_agenda, name='delete_agenda'),
]