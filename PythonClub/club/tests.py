from django.test import TestCase
from .models import Meeting, Meeting, MeetingMinutes, Resource, Event
# Create your tests here.

class MeetingClassTest(TestCase):
	def test_string(self):
		meetTest=Meeting(meetingTitle="Test Meeting")
		self.assertEqual(str(meetTest), meetTest.meetingTitle)

	def test_table(self):
		self.assertEqual(str(Meeting._meta.db_table), 'meeting')

