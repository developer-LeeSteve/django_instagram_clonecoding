from django.urls import path

from accounts import views

app_name='accounts'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.LoginView, name='login'),
]
