from django.contrib import admin
from django.urls import path
from engine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addNews/', views.addNews, name='add'),
    path('allNews/', views.allNews, name='news')
]
