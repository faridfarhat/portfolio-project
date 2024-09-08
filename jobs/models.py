from django.db import models

# Note new below code added
class Job(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=400)
    description = models.TextField()
