from django.urls import path
from post.views import (
    create_post_view,
    edit_post_view,
    detail_post_view,
    delete_post_view,
    like_post,
    unlike_post,
    likes_view,
)



app_name = 'post'

urlpatterns = [
	path('create', create_post_view, name="create_post"),
    path('<slug>/', detail_post_view, name="detail_post"),
    path('<slug>/edit', edit_post_view, name="edit_post"),
    path('<slug>/delete', delete_post_view, name="delete_post"),
	path('<slug>/like', like_post, name="like_post"),
	path('<slug>/unlike', unlike_post, name="unlike_post"),
    path('<slug>/liked', likes_view, name="likes"),

]