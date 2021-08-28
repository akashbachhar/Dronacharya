from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.handle_signup, name='handle_signup'),
    path('login/', views.handle_login, name='handle_login'),
    path('logout/', views.handle_logout, name='handle_logout'),
]
