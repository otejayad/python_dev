from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import WebappItem

# Create your views here.
def webappView(request):
    all_web_items = WebappItem.objects.all()
    return render(request,'webapp.html',
        {'all_items' : all_web_items})
        
def addWebapp(request):
    new_item = WebappItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/webapp/')
    
def deleteWebapp(request, web_id):
    #retrieve with web_id first
    item_to_delete = WebappItem.objects.get(id=web_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/webapp/')
 