from django.contrib import messages
from django.shortcuts import render
from django.views.generic.base import TemplateView


class LandingView(TemplateView):

	template_name = 'userprofile/index.html'


class DashboardView(TemplateView):

	template_name = 'userprofile/dashboard.html'


