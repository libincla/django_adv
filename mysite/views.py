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

def show_ua(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("you browser is %s" % ua )


def display_meta(request):
    values = request.META.items()
    html = []
    for i, j in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' %(i, j))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def display_whole(request):
    values = request.POST.items()
    h = []
    for x, y in values:
        h.append('<tr><td>%s</td><td>%s</td></tr>' %(x, y))
    return HttpResponse('<table>%s</table>' % h)

