from django.http import HttpResponse, HttpResponseRedirect
from houseman.models import Appliance
from django.shortcuts import render, get_object_or_404

def index(request):
    appliance_list = Appliance.objects.all()
    context = {'appliance_list': appliance_list}
    return render(request, 'houseman/index.html', context)
    
    
def switch(request, appliance_id):
    appliance = get_object_or_404(Appliance, pk=appliance_id)
    return render(request, 'houseman/switch.html', {'appliance': appliance})

def process(request, appliance_id):
    app = get_object_or_404(Appliance, pk=appliance_id)
    status = request.POST['button']
    
    if status == "on":
        app.on()
    elif status == "off":
        app.off()
        
    return HttpResponseRedirect(reverse('houseman:index', args=(app.id,)))
