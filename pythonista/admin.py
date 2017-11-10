from django.contrib import admin
from pythonista.models import Airlines, Plane, Feedback, User, journey
# Register your models here.
admin.site.register(Airlines)
admin.site.register(Plane)
admin.site.register(User)
admin.site.register(Feedback)
admin.site.register(journey)