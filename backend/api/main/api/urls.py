from django.urls import path
from auth_backend.views import RegisterAPI,LoginAPI,AdminLoginApi
from user.views import UserProfileAPI
from adminSide.views import UserViewSet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # authAPI 

    path('register/',RegisterAPI.as_view(),name="resgistrapi"),
    path('login/',LoginAPI.as_view(),name="loginapi"),


    # userAPI

    path('profile/',UserProfileAPI.as_view(), name='user_profile'),


    # admin

    path('admin/login/',AdminLoginApi.as_view(),name='admin_login'),
    path('admin/home/',UserViewSet.as_view(),name="userview"),
    path('admin/home/<int:pk>/',UserViewSet.as_view(),name="userview"),  
]

