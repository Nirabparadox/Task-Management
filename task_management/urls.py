"""
URL configuration for task_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from tasks.views import home,contact


# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("home/", home),
#     path("contact/", contact)
# ] If I did this the when I give http://127.0.0.1:8000/ then I can see that page not found(404). Because by this url there is no path. To find the page I have to give http://127.0.0.1:8000/home/    or http://127.0.0.1:8000/contact/

##But if I want to find the page but only the http://127.0.0.1:8000/ then the code of urls will looks like:
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("contact/", contact),
    path("tasks/",include("tasks.urls"))

 ] 