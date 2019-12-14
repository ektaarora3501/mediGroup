from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .views import (
    PostList,
    PostDetail,
    PostCreate,
)

urlpatterns = [
    url(r'^$', PostList.as_view(), name='posts'),
    url(r'^<slug:slug>/', PostDetail.as_view(), name='details'),
    url(r'^create/$', PostCreate.as_view(), name='post_create')
]