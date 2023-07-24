from django.urls import path
from .views import (
    get_list_video,
    get_video,
    add_like,
    add_dislike, 
    add_video,
    add_comment,
    LikeListCreateAPIView,
    CommentListApiView,
    CommentListCreateAPIView
)
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static



urlpatterns = [
    path('',get_list_video,name='home'),
    path('<int:pk>/', get_video, name='video'),
    path('<int:pk>/add-comment/', add_comment, name='comment'),
    path('<int:pk>/like/', add_like, name='like'),
    path('<int:pk>/dislike/', add_dislike, name='dislike'),
    path('add-video/', add_video, name='add-video'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentListApiView.as_view(), name='comment-list-create-pk'),
    path('likes/', LikeListCreateAPIView.as_view(), name='like-list-create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

