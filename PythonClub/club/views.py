from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, EventForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index (request):
    return render(request, 'club/index.html')

def getmeetings(request):
	meeting_list=Meeting.objects.all()
	return render(request, 'club/meetings.html' ,{'meeting_list' : meeting_list})

def meetingdetails(request, id):
	meet=get_object_or_404(Meeting, pk=id)
	context={'meet' : meet}
	return render(request, 'club/meetingdetails.html', context=context)

def getminutes(request):
	minutes_list=MeetingMinutes.objects.all()
	return render(request, 'club/minutes.html' ,{'minutes_list' : minutes_list})

def getresources(request):
	resource_list=Resource.objects.all()
	return render(request, 'club/resources.html' ,{'resource_list' : resource_list})

def getevents(request):
	event_list=Event.objects.all()
	return render(request, 'club/events.html' , {'event_list' : event_list})

@login_required
def newMeeting(request):
	form=MeetingForm
	if request.method=='POST':
		form=MeetingForm(request.POST)
		if form.is_valid():
			post=form.save(commit=True)
			post.save()
			form=MeetingForm()
	else:
		form=MeetingForm()
	return render(request, 'club/newmeeting.html', {'form': form})

@login_required
def newEvent(request):
	form=EventForm
	if request.method=='POST':
		form=EventForm(request.POST)
		if form.is_valid():
			post=form.save(commit=True)
			post.save()
			form=EventForm()
	else:
		form=EventForm()
	return render(request, 'club/newevent.html', {'form': form})

def loginmessage(request):
	return render(request, 'club/loginmessage.html')

def logoutmessage(request):
	return render(request, 'club/logoutmessage.html')

