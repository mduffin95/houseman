from django.contrib import admin
from houseman.models import Appliance, Curtain, Room, Floor

class ApplianceInline(admin.StackedInline):
    model = Appliance
    extra = 3
    
class CurtainInline(admin.StackedInline):
    model = Curtain
    extra = 1

class RoomAdmin(admin.ModelAdmin):
    inlines = [
        ApplianceInline,
        CurtainInline,
        ]

admin.site.register(Room, RoomAdmin)
admin.site.register(Floor)


