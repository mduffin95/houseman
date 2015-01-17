from django.http import HttpResponse
from houseman.models import Appliance

def index(request):
    appliance_list = Appliance.objects.all()
    output = ', '.join([p.name for p in appliance_list])
    return HttpResponse(output)
