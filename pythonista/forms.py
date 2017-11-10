from django import forms
from .models import Feedback, User, journey
class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ('name', 'email', 'comments',)
class UserRegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email',)

class BookingForm(forms.ModelForm):
	class Meta:
		model = journey
		fields = ('name', 'country', 'flight')