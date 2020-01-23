from django.urls import path 
from . views import LandingView, DashboardView



urlpatterns  = [
	path('', LandingView.as_view(), name='indexpage' ),
	path('dashboard/', DashboardView.as_view(), name='dashboard'),
]