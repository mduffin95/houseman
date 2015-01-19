from django.http import HttpResponse, HttpResponseRedirect
from houseman.models import Appliance
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

class IndexView(generic.ListView):
    model = Appliance
    template_name = 'houseman/index.html'
    
class DetailView(generic.DetailView): #named switch
    model = Appliance
    template_name = 'houseman/switch.html'
    
def process(request, appliance_id):
    app = get_object_or_404(Appliance, pk=appliance_id)
    status = request.POST['button']
    
    if status == "on":
        app.on()
        app.state = "on"
        app.save()
    elif status == "off":
        app.off()
        app.state = "off"
        app.save()
        
    return HttpResponseRedirect(reverse('houseman:index'))
