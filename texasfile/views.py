from django.shortcuts import render
from django.http import HttpResponse
import json
from texasfile.models import Resource, Image
from collections import OrderedDict

# Create your views here.
def index(request, resource_number):
    res = OrderedDict()
    resource = None
    try:
        resource = Resource.objects.get(number=resource_number)
    except Resource.DoesNotExist:
        return HttpResponse("Not Found")
    res["number"] = resource.number
    res["volume"] = resource.volume
    res["page"] = resource.page
    res["images"] = []
    images = Image.objects.filter(resource=resource)
    for i in images:
        res["images"].append(i.img)
    res = json.dumps(res)
    return HttpResponse(res, content_type="application/json")
