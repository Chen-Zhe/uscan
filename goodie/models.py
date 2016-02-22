from django.db import models

class Event(models.Model):
	title		= models.CharField(max_length=200)
#	school		= models.ManyToManyField(School)
	start		= models.DateTimeField()
	finish		= models.DateTimeField()
	code		= models.CharField(max_length=200)
	regex	    = models.TextField(default='(.*)')
	def __str__(self):
		return self.title

class Goodie(models.Model):
	matric		= models.CharField(max_length=200)
	event		= models.ForeignKey(Event)
	time		= models.DateTimeField()
	def __str__(self):
		return self.matric+" "+self.time.strftime('%Y-%m-%d %H:%M')

class School(models.Model):
	name		= models.CharField(max_length=200)
	code		= models.IntegerField()
	def __str__(self):
		return self.name

class Problem(models.Model):
	matric 		= models.CharField(max_length=200)
	school 		= models.ManyToManyField(School)
	def __str__(self):
		return self.matric