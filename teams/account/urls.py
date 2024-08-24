from django.urls import path, include


from account.views import UserLoginView, UserLogoutView, register, edit, dashboard, user_detail


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('', dashboard, name='dashboard'),
    path('users/<username>/', user_detail, name='user_detail'),
]
