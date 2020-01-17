from django.contrib import admin
from django.urls import path, include



urlpatterns = [
	path('send/', include('message.urls', namespace="sendmessage")),
    path('admin/', admin.site.urls),
]
