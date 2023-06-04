from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('videoapp.urls')),
    path('',include('users.urls'))
]

handler404 = 'videoapp.views.custom_404'