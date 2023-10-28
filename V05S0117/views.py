from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
# Create your views here.

def change_status(request,pk):
    try:
        status = Switch.objects.get(id=1)
        value_dict = {
        "1":[True, "ACTIVATED"],
        "0":[False, "DEACTIVATED"]
        }
        data = {'id': 1, 'status': value_dict[pk][0]}
        serializer = SwitchSerializer(instance=status, data=data)
        if serializer.is_valid():
            serializer.save()
        html = f"<html><body> Lockdown {value_dict[pk][1]}.</body></html>"

    except:

        html = '<html><body> <img src="https://assets-v2.lottiefiles.com/a/09bc7226-118c-11ee-a5af-1bb00158b3c0/Rd1iwPiSSM.gif" alt="404 Page Not Found" width="100%" height="100%"></body></html>'

    return HttpResponse(html)

@api_view(["GET"])
def view_status(request):
    status = Switch.objects.all()
    serializer = SwitchSerializer(status, many=True)
    return Response(serializer.data)


def api_response(request):
    return JsonResponse("API response", safe=False)


def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body> Hi {request.user.username}, It is now {now}.</body></html>"
    return HttpResponse(html)
