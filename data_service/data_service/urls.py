from django.contrib import admin
from django.urls import path

from data_app.views import upload_file, get_files, get_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_file),
    path('files/', get_files),
    path('data/<str:filename>/', get_data),
]
