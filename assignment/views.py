from django.shortcuts import render
from .models import Assignment
from dashboard.models import Subject

def assignment(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignment/assignment.html', {'assignments': assignments})


