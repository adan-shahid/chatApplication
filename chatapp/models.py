from django.db import models

# Create your models here.

class chatRooms(models.Model):
    name = models.CharField(max_length=100)
    #EACH CHATROOM IS HAVING A UNIQUE SLUG.
    slug = models.SlugField(unique=True) #WE USE THIS TO CONNECT DIFFERENT SOCKETS.
    
    def __str__(self):
        return self.name
