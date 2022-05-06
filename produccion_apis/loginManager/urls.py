from django.urls import path,include
from loginManager import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('login/',LoginView.as_view(template_name='loginManager/login.html'),name='LogIn'),
    path('logout/',LogoutView.as_view(template_name='loginManager/logout.html'),name='LogOut'),
    path('register/',views.register,name='Register'),
]