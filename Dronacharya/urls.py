from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Dronacharya Admin"
admin.site.site_title = "Dronacharya Admin"
admin.site.index_title = "Welcome to Dronacharya Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('user/', include('user.urls')),
    path('quiz/', include('quiz.urls')),
    path('assignment/', include('assignment.urls')),
]
