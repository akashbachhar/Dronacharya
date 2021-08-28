from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Subject(models.Model):
    serial = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length= 500)
    time = models.DateTimeField(default=now)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'teacher')
    enrolled = models.ManyToManyField(User, related_name='enrolled_users')

    def __str__(self):
        return self.title



