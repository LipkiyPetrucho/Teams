from django.urls import path, include


from account.views import UserLoginView, UserLogoutView, register, edit, dashboard

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('', dashboard, name='dashboard'),
]
