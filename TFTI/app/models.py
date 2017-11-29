# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	age = models.PositiveSmallIntegerField(blank=True, null=True)
	#can_drink = models.BooleanField()

	def can_drink(self):
		if age >= 21:
			return True
		else:
			return False
	#hosting = models.ForeignKey(Event, on_delete=models.CASCADE)
	#attending = models.ManyToManyField(Event)
	#tag_history = models.ForeignKey(User_Tag_Record,on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Tag(models.Model):
	tag = models.CharField(max_length=100)
	#event = models.ManyToManyField(Event)

class Profile_Tag_Record(models.Model):
	user = models.OneToOneField(Profile, on_delete=models.CASCADE)
	tag = models.OneToOneField(Tag)
	count = models.PositiveSmallIntegerField()



class Event(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	host = models.OneToOneField(Profile, on_delete=models.CASCADE)
	#guests = models.ForeignKey(Profile, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	start = models.DateTimeField(auto_now=False, auto_now_add=False)
	end = models.DateTimeField(auto_now=False, auto_now_add=False)
	alcohol = models.BooleanField()
	tags = models.ManyToManyField(Tag)
	#temporary
	location = models.TextField()

class AttendingEvent(models.Model):
	guest = models.OneToOneField(Profile, on_delete=models.CASCADE)
	event = models.OneToOneField(Event, on_delete=models.CASCADE)

	
