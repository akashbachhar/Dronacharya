from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Subject

class Meeting(models.Model):
    serial = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    meeting_link = models.CharField(max_length=200)
    time = models.DateTimeField(null = True, blank=True)


