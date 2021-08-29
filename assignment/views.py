from django.shortcuts import render
from .models import Assignment

def assignment(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignment/assignment.html', {'assignments': assignments})

def assignment_submission(request):
    return render(request, 'dashboard')


