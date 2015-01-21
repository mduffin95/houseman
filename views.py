from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from houseman.models import Appliance
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from subprocess import CalledProcessError
from time import sleep

class IndexView(generic.ListView):
    model = Appliance
    template_name = 'houseman/index.html'
    
class DetailView(generic.DetailView): #named switch
    model = Appliance
    template_name = 'houseman/switch.html'
    
def process(request, appliance_id):
    try:
        stateStr = request.POST['state']    
        app = Appliance.objects.get(pk=appliance_id)
    except (Appliance.DoesNotExist, KeyError):
        return HttpResponseBadRequest("Something went wrong. stateStr=" + stateStr)
    
    while True:
        try:
            if (app.state and stateStr == "1"): #If db says it is on and the website says it is on
                app.off()
            elif ((not app.state) and stateStr == "0"):
                app.on()
            else:
                return HttpResponseForbidden("You've pressed the button too many times. stateStr=" + stateStr + " app.state=" + str(app.state)) #This state could occur if the button is pressed too many times
            app.state = not app.state
            app.save()
            return HttpResponse("All is well.")
        except (CalledProcessError, OSError): #Might not be a good idea to catch OSError here.
            sleep(0.2)
            continue
        
    
    
'''def get_state(request, appliance_id):
    try:
        a = Appliance.objects.get(pk=appliance_id)
        if request.method == 'POST':
            form = ApplianceSwitchForm(request.POST, instance=a) #Will update the instance when saved.
            if form.is_valid():
                form.save() #Updates the state
        else:
            form = ApplianceSwitchForm(request.POST, instance=a)
    except Appliance.DoesNotExist:
        raise Http404("Appliance does not exist.")
    
    return render(request, 'houseman/switch.html', {'form': form})'''

