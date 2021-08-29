from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Subject
from assignment.models import Assignment
from meeting.models import Meeting


def dashboard(request):
    if request.user.is_authenticated:
        enrolled_subject = Subject.objects.filter(enrolled = request.user)
    else:
        enrolled_subject = "No Subject"
    return render(request, 'dashboard/dashboard.html', {'enrolled_subject': enrolled_subject})

def available_subject(request):
    subjects = Subject.objects.order_by('-time').all()
    return render(request, 'dashboard/available_subjects.html', {'subjects':subjects})

def subject_page(request, subject_id):
    subject_page = get_object_or_404(Subject, pk = subject_id)
    subject_meeting = Meeting.objects.filter(subject=subject_page)
    return render(request, 'dashboard/subject.html', {'subject_page': subject_page,
                                                      'subject_meeting':subject_meeting
                                                      })

def join(request, subject_id):
    subject = get_object_or_404(Subject, pk = subject_id)

    if subject.enrolled.filter(id = request.user.id).exists():
        subject.enrolled.remove(request.user)
        return redirect('dashboard')
    else:
        subject.enrolled.add(request.user)
        return redirect('dashboard')




