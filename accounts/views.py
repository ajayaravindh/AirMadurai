from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as alogin

# Create your views here.
def register(request):
	if(request.method == 'POST'):
		aform = UserCreationForm(request.POST)
		if(aform.is_valid()):
			user = aform.save()
			alogin(request, user)
			return redirect('/')
	else:
		aform = UserCreationForm()
	return render(request, 'accounts/register.html', {'form': aform})