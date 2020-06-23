from django import forms
from .models import Meeting, MeetingMinutes, Resource, Event

class MeetingForm(forms.ModelForm):
	class Meta:
		mtng=Meeting
		fields='__all__'_'

