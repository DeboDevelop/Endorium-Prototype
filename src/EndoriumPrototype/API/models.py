from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    banned = models.DateField()

    def __str__(self):
        return self.user_name

class AdminMap(models.Model):
    room_id = models.AutoField(primary_key=True)
    admin_id = models.OneToOneField(User, on_delete=models.CASCADE)
    phrase = models.IntegerField()

    def __str__(self):
        return self.room_id

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    room_id = models.ManyToManyField(AdminMap)
    message = models.CharField(max_length=512)
    No_of_upvote = models.IntegerField()
    
    def __str__(self):
        return self.message_id

class Upvote(models.Model):
    message_id = models.ManyToManyField(Message)
    room_id = models.ManyToManyField(AdminMap)
    user_id = models.ManyToManyField(User)


    def __str__(self):
        return (self.user_id + " " + self.message_id)
