from django.db import models

class Content(models.Model):
    content = models.CharField(default="student", max_length=99, null=False)

class UserInfo(models.Model):
    userName = models.CharField(max_length=255, null=False)
    contact = models.CharField(max_length=20, null=False)  # Adjust max_length as needed
    upiId = models.CharField(max_length=255, null=False)



class Purpose(models.Model):
    title = models.CharField(max_length=255, null=False)
    paidBy = models.CharField(max_length=377,null=False) # Assuming paidBy is a user
    paidAmount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    splitedAmount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
