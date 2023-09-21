
from django.urls import path
from . import views

urlpatterns = [
    path('create_section/', views.create_section, name='create_section'),
    path('class_section_count/', views.class_section_count, name='class_section_count'),
    # Add other URL patterns as needed
]
