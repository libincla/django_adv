from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from books.models import Book
from books.forms import ContactForm
from django.core.mail import send_mail

from django.template import loader, RequestContext 

from django.views.generic import ListView, DetailView
from books.models import Publisher, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

class PublisherList(ListView):
    model = Publisher

class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'

#class PublisherDetail(DetailView):
#    model = Publisher
#
#    def get_context_data(self, **kwargs):
#        context = super(PublisherDetail, self).get_context_data(**kwargs)
#        context['book_list'] = Book.objects.all()
#        return context
         

def my_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/search-form/')
            else:
                return HttpResponse('your account is not active')
        else:
            return HttpResponse('invalid login, you need sign up first')

    else:
        return render(request, 'registration/login.html', {})


def logout_view(request):
    logout(request)
    return  HttpResponseRedirect('/dw/')


def email_check(user):
    return user.email.endswith('@qq.com')



@login_required(login_url='/login/')
def search_form(request):
    user = request.user
    #user = request.POST.get('username')
    return render(request, 'search_form.html', {'username' : user })



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


@user_passes_test(email_check, login_url='/hi/')
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
