from django.db import models

class Complaint(models.Model):
	complaintnumber = models.IntegerField(max_length=5)
	fname = models.CharField(max_length=15)
	lname = models.CharField(max_length=15)
	gender = models.CharField(max_length=6)
	date = models.DateField(max_length=10)
	mail = models.EmailField(max_length=256)
	pno = models.IntegerField(max_length=10)
	add = models.CharField(max_length=200)
	desc = models.CharField(max_length=500)
	status=models.CharField(max_length=20)
	complaint=models.Manager()


class Auth(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	auth= models.Manager()
	
class Crime(models.Model):
	crimenumber =models.IntegerField(max_length=5)
	fname = models.CharField(max_length=15)
	lname = models.CharField(max_length=15)
	crime = models.CharField(max_length=200)
	age = models.IntegerField(max_length=2)
	crimes= models.Manager()
