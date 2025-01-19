from django.urls import path
from . import views

urlpatterns = [
    path('Questions/', views.Questions, name='Questions'),
]
