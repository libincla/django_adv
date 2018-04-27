from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from django.template.loader import get_template
import datetime



def hi(request):
    return HttpResponse('hi wolrd!')

#def current_datetime(request):
#    now = datetime.datetime.now()
#    now = str(now)[:-7]
#    html = "it is %s now." % now
#    return HttpResponse(html)

#def current_datetime(request):
#    now = datetime.datetime.now()
#    now = str(now)[:-7]
#    t = get_template('current_datetime.html')
#    html = t.render(Context({'current_date': now }))
#    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    now = str(now)[:-7]
    return render(request, 'current_datetime.html', {'current_date' : now })



def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        offset = int(0)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    dt = str(dt)[:-7]
    html = "in %s hour, it will be %s." % (offset, dt)
    context_dict = {'hour_offset' : offset, 'next_time' : dt }
    return render(request, 'hours_ahead.html', context=context_dict)
