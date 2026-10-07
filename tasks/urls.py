from django.contrib import admin
from django.urls import path
from tasks.views import show_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_task/', show_task)
]