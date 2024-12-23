from django.urls import include,path,re_path
from . import views
from django.contrib import admin


urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:pk>/edit/',views.post_edit,name='post_edit'),
    path('drafts/',views.post_draft_list,name='post_draft_list'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),
    path('post/<int:pk>/remove/',views.post_remove,name='post_remove'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post,name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    re_path(r'/comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
]