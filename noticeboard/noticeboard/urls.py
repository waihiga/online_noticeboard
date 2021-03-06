from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('accounts.urls')),
    path('', include('accounts.users_urls')),
    path('', include('roles.urls')),
    path('', include('permissions.urls')),
    path('', include('posts.urls')),
    path('', include('departments.urls'))
]
