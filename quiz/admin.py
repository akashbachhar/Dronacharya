from django.contrib import admin

from .models import Quiz, Question, Answer, Result

admin.site.register((Quiz, Question, Answer, Result))
