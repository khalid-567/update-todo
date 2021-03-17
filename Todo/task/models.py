from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Customer(models.Model):
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    email=models.EmailField()
    added_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.first_name





class Task(models.Model):
 	serial_number= models.IntegerField()
 	task_due_date= models.DateTimeField(auto_now_add=True)
 	task= models.CharField(max_length=100)
 	added_by= models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
 	complete= models.BooleanField(default=False)


 	def __str__(self):
 		return self.task





class Note(models.Model):
 	serial_number= models.IntegerField()
 	date= models.DateTimeField(auto_now_add=True)
 	note= models.TextField()
 	added_by= models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)


 	def __str__(self):
 		return self.note


