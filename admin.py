from django.contrib import admin
from houseman.models import *

class DefaultInline(admin.StackedInline):
    model = DefaultApp
    extra = 1
    
class CurtainInline(admin.StackedInline):
    model = Curtain
    extra = 1

class RoomAdmin(admin.ModelAdmin):
    inlines = [
        DefaultInline,
        CurtainInline,
        ]

admin.site.register(Room, RoomAdmin)
admin.site.register(Floor)


