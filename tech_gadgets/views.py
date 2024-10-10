from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from django.utils.text import slugify
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json

from .dummy_data import gadgets
# Create your views here.

def start_page_view(request):
    return HttpResponse("läuft!")

def single_gadget_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]['name'])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound('not found')

def single_gadget_slug_view(request, gadget_slug):
    gadget_match = None
    for gadget in gadgets:
        if slugify(gadget['name']) == gadget_slug:
            gadget_match = gadget
    if gadget_match: 
        return JsonResponse(gadget_match)
    raise Http404()

@csrf_exempt
def single_gadget_post_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"recived data: {data}")
            return JsonResponse({"response": 'Läuft'})
        except Exception:
            return JsonResponse({"response": 'Läuft nicht'})
    return HttpResponse('Die verwendete request.method lautet ' + request.method)