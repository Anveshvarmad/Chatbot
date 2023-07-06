from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('insetuser/',views.insertuser,name='insertuser'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('chat/', views.chat, name='chat')

]