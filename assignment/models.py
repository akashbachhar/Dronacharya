from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from dashboard.models import Subject

class Assignment(models.Model):
    serial = models.AutoField(primary_key = True)
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
    status = models.BooleanField(default=True)
    creation_time = models.DateTimeField(default=now)
    submission_time = models.DateTimeField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    description = models.TextField(blank=True)



