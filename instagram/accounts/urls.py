from django.urls import path

from accounts import views

app_name='accounts'

urlpatterns = [
	path('', views.index, name="index"),
    path('accounts/register/', views.UserRegisterView.as_view(), name='register'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('accounts/email_verification_code/', views.EmailVerificationView.as_view(), name='email_verification_code'),
    path('register_email/', views.RegisterEmail, name='register_email'),
    path('inbox/', views.inbox, name='inbox'),
    path('activity/', views.activity, name='activity'),
    path('explore/', views.explore, name='explore'),
    path('accounts/<str:username>/', views.profile, name="profile"),
]
