from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import re
import json

from django.utils import timezone
from goodie.models import *

from goodie.forms import GoodieForm


def index(request):
    return HttpResponse("hello")

def check_event(request,event_code):
    try:
        event = Event.objects.get(code=event_code)
    except Event.DoesNotExist:
        return HttpResponse('false')

    return_object = {"title": event.title, "regex": event.regex}

    return HttpResponse(json.dumps(return_object))


def list_matric(request,event):
    try:
        event = Event.objects.get(code=event)
    except Event.DoesNotExist:
        return HttpResponse('false')

    register_entries = Goodie.objects.filter(event=event)

    matric_list = []
    for entry in register_entries:
        matric_list.append({'matric': entry.matric, 'time':entry.time.strftime('%a %b %d %H:%M:%S %Y')})

    return HttpResponse(json.dumps(matric_list))


def manual_register(request,event):
    try:
        Event.objects.get(code=event)
    except Event.DoesNotExist:
        return HttpResponse('Incorrect Event Code')

    if request.method == 'GET':
        form = GoodieForm()
    else:
        fail_reason = "exist in the database"
        form = GoodieForm(request.POST)
        if form.is_valid():
            matric = form.cleaned_data['matric'].upper()
            success = False
            if re.match(Event.objects.get(code=event).regex,matric):
                try:
                    Goodie.objects.get(matric=matric,event= Event.objects.get(code=event))
                except Goodie.DoesNotExist:
                    tmp = Goodie(matric=matric, event= Event.objects.get(code=event), time=timezone.now())
                    tmp.save()
                    success = True
            else:
                fail_reason = "invalid matric number for this event"
            form = GoodieForm()
            return render(request, 'input.html', {'form': form, 'success': success, 'matric': matric, 'reason':fail_reason})
    return render(request, 'input.html', {'form': form,})


def register(request, matric_number, event):

    matric_number = matric_number.upper()
    try:
        Event.objects.get(code= event)
    except Event.DoesNotExist:
        return HttpResponse(json.dumps({"flag": False, "message": "Invalid event code"}))

    try:
        Goodie.objects.get(matric=matric_number,event= Event.objects.get(code=event))
    except Goodie.DoesNotExist:
        if not re.match(Event.objects.get(code=event).regex, matric_number):
            return HttpResponse(json.dumps({"flag": False, "message": "Invalid matric for this event"}))
        tmp = Goodie(matric=matric_number, event= Event.objects.get(code=event), time=timezone.now())
        tmp.save()
        return HttpResponse(json.dumps({"flag": True, "message": 'New input success! matric : {0} , event : {1}'.format(matric_number,Event.objects.get(code=event).title)}));

    return HttpResponse(json.dumps({"flag": False, "message": 'This matric is already registered for this event'}))