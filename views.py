from django.http import HttpResponse, HttpResponseRedirect
from houseman.models import Appliance
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
import sys, subprocess

class IndexView(generic.ListView):
    model = Appliance
    template_name = 'houseman/index.html'
    
class DetailView(generic.DetailView): #named switch
    model = Appliance
    template_name = 'houseman/switch.html'
    
def process(request, appliance_id):
    try:
        #checkState = request.POST['state']
        app = Appliance.objects.get(pk=appliance_id)
    except (Appliance.DoesNotExist):
        return HttpResponse("The key was not found.")
    
    while True:
        try:
            if app.state:
                app.off()
                print("Turning off")
            else:
                app.on()
                print("Turning on")
            app.state = not app.state
            app.save()
            print("About to break")
            sys.stdout.flush()
            break
        except (subprocess.CalledProcessError, OSError):
            print("Still running, looping now")
            continue
        
    return HttpResponseRedirect(reverse('houseman:index'))
    
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

