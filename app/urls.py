# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('index/', views.index, name='index'),  # Main application
    path('add/', views.add, name='add'),
    path('addrec/', views.addrec, name='addrec'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('uprec/<int:id>/', views.uprec, name='uprec'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('signout/', views.signout_view, name='signout'),
]
