from subprocess import call
from django.db import models

class Floor(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(unique=True, default=0)
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.ForeignKey(Floor)
    
    def __str__(self):
        return self.name
    
class Appliance(models.Model):
    name = models.CharField(max_length=200)
    lirc_dev = models.CharField('lirc device name', max_length=200)
    create_date = models.DateTimeField('date created')
    room = models.ForeignKey(Room)
    state = models.BooleanField()
    
    def __str__(self):
        return self.name
        
    def on(self):
        call(["irsend","SEND_START",self.lirc_dev,"on"])
        
    def off(self):
        call(["irsend","SEND_START",self.lirc_dev,"off"])
    

        

        
    
