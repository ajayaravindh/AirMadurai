from django.conf.urls import url
from pythonista import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'users/', views.list_users, name = 'list_users'),
	url(r'feedback/', views.feedback_view, name = 'feedback'),
	url(r'register/', views.user_registration, name = 'user_registration'),
	url(r'book/', views.book, name = "book"),
	url(r'brogrammerz/', views.we_the_brogrammerz, name = "brogrammerz"),
]