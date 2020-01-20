from django.contrib import admin
from django.urls import path, include



urlpatterns = [
	path('', include("userprofile.urls")),
	path('send/', include('message.urls', namespace="sendmessage")),
    path('admin/', admin.site.urls),
]
