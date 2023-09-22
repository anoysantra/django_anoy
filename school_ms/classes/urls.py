from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list, name='class_list'),
    path('add_class/', views.add_class, name='add_class'),
    path('edit_class/<str:class_name>/', views.edit_class, name='edit_class'),
    path('delete_class/<str:class_name>/', views.delete_class, name='delete_class'),
]
