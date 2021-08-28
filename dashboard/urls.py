from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('available_subject/', views.available_subject, name='available_subject'),
    path('<int:subject_id>', views.join, name = 'join')
]