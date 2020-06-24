from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, EventForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
		self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
		self.meet=Meeting.objects.create(meetingTitle='testmeeting')

#	def test_redirect_if_not_logged_in(self):
#		response=self.client.get(reverse('newmeeting'))
#		self.assertRedirects(response, '/accounts/login/?next=/club/newmeeting/')

	def test_Logged_in_uses_correct_template(self):
		login=self.client.login(username='testuser1', password='P@ssw0rd1')
		response=self.client.get(reverse('newmeeting'))
		self.assertEqual(str(response.context['user']), 'testuser1')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'club/newmeeting.html')

