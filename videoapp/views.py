from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Video, Comment, Like, Dislike
from users.models import UserProfile
from .serializers import CommentSerializer, LikeSerializer, DislikeSerializer

class CommentListApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        video_pk = self.kwargs.get('pk')
        queryset = Comment.objects.filter(video__pk=video_pk)
        return queryset

    serializer_class = CommentSerializer

class CommentListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer

class LikeListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        video_pk = self.kwargs.get('pk')
        queryset = Like.objects.filter(video__pk=video_pk)
        return queryset

    serializer_class = LikeSerializer

class LikeListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class DislikeListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        video_pk = self.kwargs.get('pk')
        queryset = Dislike.objects.filter(video__pk=video_pk)
        return queryset

    serializer_class = DislikeSerializer

class DislikeListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer

    
def get_list_video(request):
    video_list = Video.objects.all()
    context = {
        'video_list':video_list,
        'user': request.user
    }
    return render(request, 'videoapp/home.html', context )

def get_video(request, pk:int):
    _video = get_object_or_404(Video,id=pk)
    likes_count = Like.objects.filter(video__pk=pk).count()
    dislikes_count = Dislike.objects.filter(video__pk=pk).count()
    current_user = request.user.username
    return render(request,'videoapp/video.html', {'video' : _video, "current_user" : current_user, "video_id": pk, 'likes_count':likes_count, 'dislikes_count':dislikes_count})

def add_video(request):
    context = {
        'user': request.user
    }
    if request.method == 'POST':
        print(request.FILES)
        video_file = request.FILES['video-file']
        video_thumbnail = request.FILES['video-thumbnail']
        description = request.POST['video-description']
        video_title = request.POST['video-title']
        User = get_user_model()
        user = User.objects.get(pk=request.user.pk)
        try:
            profile = user.userprofile
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=user)

        video = Video(title=video_title, file=video_file, image=video_thumbnail, description=description, user=profile.user)
        video.save()    
        return redirect('home')

    return render(request, 'videoapp/add-video.html', context)

def add_comment(request, pk):
    video = get_object_or_404(Video, pk=pk)
    context = {
        'video':video
    }
    if request.method == "POST":
        comment_body = request.POST.get('comment')
        comment = Comment(body=comment_body, video=video, user=request.user)
        comment.save()
        return redirect('video', pk=pk)

    return render(request, 'videoapp/video.html', context)

def add_like(request, pk):
    video = get_object_or_404(Video, pk=pk)
    like = Like.objects.filter(video=video).filter(user=request.user)
    context = {
        'video': video,
    }
    
    if request.method == "POST":
        if 'likes' in request.POST and not like.exists():
            Like.objects.create(video=video, user=request.user)
            Dislike.objects.filter(video=video, user=request.user).delete()
        elif 'likes' in request.POST and like.exists():
            like.delete()
        return redirect('video', pk=pk)
    video.save()
    
    return render(request, 'videoapp/video.html', context)

def add_dislike(request, pk):
    video = get_object_or_404(Video, pk=pk)
    dislike = Dislike.objects.filter(video=video).filter(user=request.user)
    context = {
        'video':video,
    }

    if request.method == "POST":
        if 'dislikes' in request.POST and not dislike.exists():
            Dislike.objects.create(video=video, user=request.user)
            Like.objects.filter(video=video, user=request.user).delete()
        elif 'dislikes' in request.POST and dislike.exists():
            dislike.delete()
        return redirect('video', pk=pk)
    video.save()
    
    return render(request, 'videoapp/video.html', context)

def custom_404(request,exception):
    return render(request,'videoapp/errors/404.html', status=404)


