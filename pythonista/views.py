from django.shortcuts import render
from django.contrib.auth .models import User
from .forms import FeedbackForm, UserRegistrationForm, BookingForm
# Create your views here.
def index(request):
	return render(request, 'pythonista/home.html', {})

def list_users(request):
	users = User.objects.all()
	return render(request, 'pythonista/list_users.html', {'users': users})

def feedback_view(request):
	if (request.method == "POST"):
		f = FeedbackForm(request.POST)
		if (f.is_valid()):
				f = f.save()
				#post.save()
	else:
		f = FeedbackForm()
	return render(request, 'pythonista/feedback.html', {'form': f})

def user_registration(request):
	if(request.method == "POST"):
			f = UserRegistrationForm(request.POST)
			if(f.is_valid()):
				p = f.save()
				p.save()
				return render(request, 'pythonista/home.html')
	else:
		f = UserRegistrationForm()
	return render(request, 'pythonista/user_registration.html', {'form': f})

def book(request):
	if(request.method == "POST"):
		f = BookingForm(request.POST)
		if(f.is_valid()):
			p = f.save()
			p.save()
			return render(request, 'pythonista/home.html')
	else:
		f = BookingForm()
	return render(request, 'pythonista/book.html', {'form': f})

def we_the_brogrammerz(request):
	return render(request, 'pythonista/brogrammerz.html')