from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display_time(request):
    date=datetime.datetime.today()
    h=int(date.strftime('%H'))
    msg='Hello!, Good '
    if h<12:
        msg=msg+'Morning'
    elif h<16:
        msg=msg+'Afternoon'
    elif h<21:
        msg=msg+'Evening'
    else:
        msg=msg+'Night'
    return HttpResponse(msg+' and now the server time is :'+str(date))

# Create your views here.
