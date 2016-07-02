from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	Uid = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 30)
	phonenumber =models.CharField(max_length=100)
	email = models.EmailField()
	address = models.TextField(max_length=100)
	password = models.CharField(max_length=50)

	def __unicode__(self):
		return u"%s"%(self.name)

	def is_authenticated(self):
		return True

class Experience(models.Model):
	user = models.ForeignKey(User,related_name='user_experience')
	starttime = models.DateField()
	endtime = models.DateField()
	company = models.CharField(max_length = 30)
	position = models.CharField(max_length = 30)
	content = models.TextField(max_length = 3000)

	def __unicode__(self):
		return u"%s"%self.company

class skill(models.Model):
	user = models.ForeignKey(User,related_name='user_skill')
	skillname = models.TextField(max_length=300)

	def __unicode__(self):
		return u"%s"%self.skillname

class Education(models.Model):
	user = models.ForeignKey(User,related_name='user_Education')
	starttime = models.DateField()
	endtime = models.DateField()
	school = models.TextField(max_length=30)
	content = models.TextField(max_length=3000)

	def __unicode__(self):
		return u"%s"%self.school

class introduction(models.Model):
	user = models.ForeignKey(User,related_name='user_introduction')
	content = models.TextField(max_length=100)

	def __unicode__(self):
		return u"%s"%self.user,u"%s"%self.introduction






