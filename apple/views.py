from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import person,order,comment
from .forms import person_form,order_form,comment_form
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

def index(request):
    return HttpResponse('sidhu')

class creat_user(CreateView):

    model = person
    form_class = person_form
    template_name = 'user/person.html'
    success_url = '/'
    success_message = 'Employee successful created'


def fun_creat_user(request):

    if request.method == 'POST':
        fm = person_form(request.POST)
        if fm.is_valid():
            fm.save()
        else:
            print('error')

    else:
        fm = person_form()
    context = {'form':fm}
    return render(request,'user/person.html',context)


