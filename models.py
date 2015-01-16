from subprocess import call
from django.db import models

class Floor(models.Model):
    name = models.CharField(max_length=200)
    
class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.ForeignKey(Floor)
    
class Appliance(models.Model):
    name = models.CharField(max_length=200)
    lirc_dev = models.CharField('lirc device name', max_length=200)
    create_date = models.DateTimeField('date created')
    room = models.ForeignKey(Room)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
        
    def on(self):
        call(["irsend","SEND_START",lirc_dev,"on"])
        
    def off(self):
        call(["irsend","SEND_START",lirc_dev,"off"])
    
    #Could add this later to allow different types of switch, eg. dimmers.
    #class Meta:
    #    abstract = True
        

        
    
