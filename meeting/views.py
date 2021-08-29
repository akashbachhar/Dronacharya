from django.shortcuts import render
from .models import Meeting


def meeting(request):
    meetings = Meeting.objects.all()
    return render(request, 'meeting/meeting.html', {'meetings': meetings})
