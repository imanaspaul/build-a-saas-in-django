from django.db import models
from django.contrib.auth.models import User


# User's contact form model

class Message(models.Model):

	fname = models.CharField(max_length=40)
	lname = models.CharField(max_length=40)
	subject = models.CharField(max_length=100)
	body = models.TextField(max_length=1000)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)



	def __str__(self):

		return f"{self.owner.username}'s mail {self.subject}"


# Email sending Count

class CountEmail(models.Model):

	count = models.IntegerField(default=0)
	owner_email = models.EmailField(max_length=254)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.owner}'s count is {self.count}"