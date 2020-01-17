from django.urls import path
from . views import sendmail, success


app_name = "sendmessage"

urlpatterns = [
	# path('<id>/', sendmail, name='sendmail'),
	path('success/', success, name='success'),
	path('user/<id>/', sendmail, name='sendmail'),
]