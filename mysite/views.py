from django.http import HttpResponse
import datetime



def hi(request):
    return HttpResponse('hi wolrd!')

def current_datetime(request):
    now = datetime.datetime.now()
    now = str(now)[:-7]
    html = "it is %s now." % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        offset = int(0)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    dt = str(dt)[:-7]
    html = "in %s hour, it will be %s." % (offset, dt)
    return HttpResponse(html)
