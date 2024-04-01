from django.urls import path
from . import views 

urlpatterns = [
    
    path('blog/create', views.create, name='create'),
    path ('blog/home', views.home, name='home'),  
    path('blog/<int:blog_id>', views.detail, name='detail'),
]