from django.shortcuts import render, redirect
from django.http import HttpResponse




def sendmail(request, id):

	# collect the querry parameters that has been send from the client
	print(id)
	name = request.GET.get("name")
	email = request.GET.get("email")
	#	context = {""}
	return redirect('sendmessage:success')


def success(request):

	return render(request, 'message/success.html')