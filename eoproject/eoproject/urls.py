from django.contrib import admin
from django.urls import path
from eoapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
]

handler404 = "eoapp.views.pnf"