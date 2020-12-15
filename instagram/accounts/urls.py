from django.urls import path

from accounts import views

app_name='accounts'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logoutUser, name='logout'),
    path('email_verification_code/', views.EmailVerificationView.as_view(), name='email_verification_code')
]
