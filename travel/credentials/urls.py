from . import views
from django.urls import path

urlpatterns = [
    path('regis',views.regis,name='regis'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]
