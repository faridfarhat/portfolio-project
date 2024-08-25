from django.contrib import admin

# Note below added
from .models import Job
admin.site.register(Job)
