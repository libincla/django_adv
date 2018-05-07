from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from books.models import Book
from books.forms import ContactForm
from django.core.mail import send_mail

from django.template import loader, RequestContext 

# Create your views here.

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    #error = False
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('plz input sth')
        elif len(q) > 20:
            errors.append('length not large than 20 words')
        else: #the request of q is valid 
            books = Book.objects.filter(title__istartswith=q)
            return render(request, 'search_results.html', {'books' : books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'], cd['message'], cd.get('email', 'libin@huitongjy.com'), ['libin@huitongjy.com'], )
            #return HttpResponseRedirect('/contact/thanks/')
            return render(request, 'search_form.html', {})
    else:
        form = ContactForm( initial={'subject' : 'how do you do?'})
    return render(request, 'contact_form.html', {'form' : form})

def mytest(request, testid="3"):
    return HttpResponse('<h1> this is %r </h1>' % testid)

def custom_proc(request):
    return {
        'app' : 'my app',
        'user' : request.user,
        'ip_address' : request.META['REMOTE_ADDR']
    }


def view1(request):
    t = loader.get_template('template1.html')
    c = RequestContext(request, {'message': 'view1'}, processors=[custom_proc])
    return t.render(c)

 
def view2(request):
    t = loader.get_template('template2.html')
    c = RequestContext(request, {'message': 'view2'}, processors=[custom_proc])
    return t.render(c)
