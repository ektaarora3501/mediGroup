from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    PostList,
    PostDetail,
    PostCreate,
)

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('<slug:slug>/', PostDetail.as_view(), name='details'),
    path('create/$', PostCreate.as_view(), name='create')
]