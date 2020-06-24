from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm,EventForm

# Model Tests

class MeetingClassTest(TestCase):
	def test_string(self):
		meetTest=Meeting(meetingTitle="Test Meeting")
		self.assertEqual(str(meetTest), meetTest.meetingTitle)

	def test_table(self):
		self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesClassTest(TestCase):
	#def test_string(self):
	#	meetMinTest=MeetingMinutes(meetingTitle="Another Test Meeting")
	#	self.assertEqual(str(meetMinTest), meetMinTest.meetingTitle)

	def test_table(self):
		self.assertEqual(str(MeetingMinutes._meta.db_table), 'minutes')

class ResourceClassTest(TestCase):
	def test_string(self):
		resTest=Resource(resourceName="Test Resource")
		self.assertEqual(str(resTest), resTest.resourceName)

	def test_table(self):
		self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventClassTest(TestCase):
	def test_string(self):
		eventTest=Event(eventTitle="Test Event")
		self.assertEqual(str(eventTest), eventTest.eventTitle)

	def test_table(self):
		self.assertEqual(str(Event._meta.db_table), 'event')

# Form Tests



class MeetingFormTest(TestCase):
#	def test_meetform_minus_descript(self):
#		form=MeetingForm(data={'meetingTitle': "title1"})
#		self.assertTrue(form.is_valid())

	def test_meetform_empty(self):
		form=MeetingForm(data={'meetingTitle': ""})
		self.assertFalse(form.is_valid())

# Auth Tests

class New_Meeting_authentication_test(TestCase):
	def setUp(self):
		self.test_user-User.objects.create_user(username='testuser1', password='P@ssw0rd1')
		self.meet=Meeting.objects.create(meetingTitle='testmeeting')
		self.event=Event.objects.create(eventTitle='event1', eventLocation=self
