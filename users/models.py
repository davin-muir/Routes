from django.db import models
from django.contrib.auth.models import User
 
 
# This model extends Django's built-in User model.
class UserProfile(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True)

    address = models.CharField(verbose_name='Address', max_length=100, null=True, blank=True)
    town = models.CharField(verbose_name='Town/City', max_length=100, null=True, blank=True)
    county = models.CharField(verbose_name='County', max_length=100, null=True, blank=True)
    post_cde = models.CharField(verbose_name='Post Code', max_length=100, null=True, blank=True)
    country = models.CharField(verbose_name='Country', max_length=100, null=True, blank=True)
    longitude = models.CharField(verbose_name='Longitude', max_length=100, null=True, blank=True)
    latitude = models.CharField(verbose_name='Latitude', max_length=100, null=True, blank=True)

    has_profile = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    # When someone submits a form on sign-up, we'll store the ReCpatcha score in this field.
    captcha_score = models.FloatField(default = 0.0)

    def __str__(self):
        return f'{self.user}'