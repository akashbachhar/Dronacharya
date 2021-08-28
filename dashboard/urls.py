from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('available_subject/', views.available_subject, name='available_subject'),
    path('<int:subject_id>', views.join, name = 'join')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)