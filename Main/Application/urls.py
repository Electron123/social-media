from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path(r'signup/', views.signup, name="signup"),
    path(r'logout/', views.log_out, name='logout'),
    path(r'post/', views.post, name='post')
]
