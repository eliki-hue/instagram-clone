
from django.test import TestCase


# Create your tests here.
from .models import Profile
class ProfileTestClass(TestCase):

    def setUp(self):
        self.new_profile =Profile('','','','','')

    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
        

    def test_updating(self):
        self.new_profile.update_profile('test_profile','test_profile2')
        self.assertFalse(Profile.objects.filter(name='test_profile2').exists())

    def test_delete_profile(self):       
        self.new_profile.delete_profile('test_profile')           
        self.assertFalse(Profile.objects.filter(name='test_profile').exists())

