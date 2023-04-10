from django.urls import path
from .views import UserAuthViewSet

urlpatterns = [
    path('register/', UserAuthViewSet.as_view({'post': 'register'}) , name='Userregister'),
    path('login/', UserAuthViewSet.as_view({'post': 'login'}) , name='Userlogin'),
    path('user/', UserAuthViewSet.as_view({'get': 'user_detail', 'patch': 'update'}) , name='UserProfile'),
    path('password_update/', UserAuthViewSet.as_view({'patch': 'password_update'}) , name='UserPasswordUpdate'),
    path('user_list/', UserAuthViewSet.as_view({'get': 'user_list'}) , name='UserList'),
]
