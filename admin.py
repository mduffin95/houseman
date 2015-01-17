from django.contrib import admin
from houseman.models import Appliance, Room, Floor

class ApplianceInline(admin.StackedInline):
    model = Appliance
    extra = 3

class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['floor']}),
    ]
    inlines = [ApplianceInline]

admin.site.register(Room, RoomAdmin)
admin.site.register(Floor)


