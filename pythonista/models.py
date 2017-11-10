from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Airlines(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Plane(models.Model):
	flight_no = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = "Unique number for this flight\n")
	capacity = models.IntegerField()
	carrier = models.ForeignKey('Airlines', on_delete = models.SET_NULL, null = True)
	user = models.ManyToManyField('User')
	places = (
			('Madurai', 'Madurai'),
			('New Delhi', 'New Delhi'),
			('New York', 'New York'),
			('Paris', 'Paris'),
			('Singapore', 'Singapore'),
			('Chennai', 'Chennai')
		)
	source = models.CharField(max_length = 20, choices = places, default = 'Madurai')
	destination = models.CharField(max_length = 20, choices = places, default = 'Chennai')
	status_str = (
			('A', 'Available'),
			('F', 'Full'),
			('N', 'Not Open'),
		)
	status = models.CharField(max_length = 1, choices = status_str, default = 'A', )
	def __str__(self):
		return '{} - {}'.format(self.source, self.destination)
class User(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	age = models.IntegerField()
	email = models.EmailField()
	profile_pic = models.ImageField()
	def __str__(self):
		return self.first_name
class Feedback(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField()
	comments = models.TextField()
class journey(models.Model):
	name = models.CharField(max_length = 50)
	country = models.CharField(max_length = 30)
	flight = models.ForeignKey('Plane', on_delete = models.SET_NULL, null = True)
	def __str__(self):
		return str(self.flight)