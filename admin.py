from django.contrib import admin
from houseman.models import Appliance, Room, Floor

class ChoiceInLine(admin.StackedInLine):
    model = Appliance
    extra = 3

class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['floor']}),
    ]
    inlines = [ChoiceInLine]

admin.site.register(Room, RoomAdmin)
#admin.site.register(Floor)


