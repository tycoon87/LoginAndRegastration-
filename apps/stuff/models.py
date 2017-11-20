from __future__ import unicode_literals
from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        message = {}
        if not EMAIL_REGEX.match(postData['Email']):
            message["mustemail"] = "Please enter a valid email!"
        if len(postData['Firstname']) < 5:
            message["lenFirstname"] = "First name should be more than 5 characters"
        if len(postData['Lastname']) < 5:
            message["lengLastname"] = "Last name should be more than 5 characters"
        if not len(postData['Firstname']):
            message["reqfirstname"] = " firstname is required!"
        if not len(postData['Lastname']):
            message["reqLastname"] = "Lastname is required!"
        if not len(postData['Email']):
            message["Email"] = "Email is required!"
        user = User.objects.filter(Email = postData['Email'])
        if user:
            message["emailexsis"] = "Sorry email already exist!"
        if len(postData['Password']) < 8:
            message["Password"] = "Blog desc should be more than 10 characters"
        if not postData['Password'] == postData['ConfirmPassword']:
            message["Email"] = "Passwors must match!"
        if message:
            return message
        else:
            newPassword = bcrypt.hashpw(postData['Password'].encode(),bcrypt.gensalt())
            user = self.create(Firstname = postData['Firstname'] , Lastname = postData['Lastname'],Email = postData['Email'], Password = newPassword)
            return message

    def LoginValidation(self, postData):
        message = {}
        user = User.objects.filter(Email=postData['Email'])
        if user:
            db_hashed = user[0].Password
            if db_hashed == bcrypt.hashpw(postData['Password'].encode(), db_hashed.encode()):
                message['status'] = "True"
                message['user'] = user[0]
                return message
        else:

            return message

    def Edit_user(self, postData):
                message = {}
                if not EMAIL_REGEX.match(postData['Email']):
                    message["mustemail"] = "Please enter a valid email!"
                if len(postData['Firstname']) < 5:
                    message["lenFirstname"] = "First name should be more than 5 characters"
                if len(postData['Lastname']) < 5:
                    message["lengLastname"] = "Last name should be more than 5 characters"
                if not len(postData['Firstname']):
                    message["reqfirstname"] = " firstname is required!"
                if not len(postData['Lastname']):
                    message["reqLastname"] = "Lastname is required!"
                if not len(postData['Email']):
                    message["Email"] = "Email is required!"
                user = User.objects.filter(Email = postData['Email'])
                if user:
                    message["emailexsis"] = "Sorry email already exist!"
                if message:
                    return message
                else:
                    u = User.objects.get(id=User_id)
                    u.Firstname = request.POST['Firstname']
                    u.Lastname = request.POST['Lastname']
                    u.Email= request.POST['Email']
                    u.save()
                    return message

class User(models.Model):
      objects = BlogManager()
      Firstname = models.CharField(max_length=255)
      Lastname = models.CharField(max_length=255)
      Email = models.CharField(max_length=255)
      Password = models.CharField(max_length=255)
       # = models.booleanField(default = true)


      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = BlogManager()
