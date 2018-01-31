from django.db import models

# Create your models here.
class Topic(models.Model):
	Top_name = models.CharField(max_length=264,unique=True)

	def __str__(self):
		return self.Top_name

class Web(models.Model):
	topic = models.ForeignKey(Topic)
	name = models.CharField(max_length=264,unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.name	

class Access(models.Model):
	name = models.ForeignKey(Web)
	date = models.DateField()
	 # url = models.URLField()

	def __str__(self):
		return str(self.date)

class User(models.Model):
	name = models.CharField(max_length=264)
	lname = models.CharField(max_length=128)
	email = models.EmailField(max_length=264,unique=True)
 	 # url = models.URLField()
