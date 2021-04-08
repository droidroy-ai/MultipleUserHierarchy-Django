from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError

from .forms import ContactUsForm
# Create your views here.


# def index(request):           // just a test function view
#     age = 10
#     arr = ['roy', 'swap', 'rhyes']
#     dic = {'a':'one', 'b':'two'}

#     return render(request, 'firstapp/index.html', {'age' : age, 'array':arr, 'dic':dic})

class Index(TemplateView):
    template_name = "firstapp/index.html"

    def get_context_data(self, **kwargs):
        age = 10
        arr = ['roy', 'swap', 'rhyes']
        dic = {'a':'one', 'b':'two'}
        context_old = super().get_context_data(**kwargs)
        context = {'age' : age, 'array':arr, 'dic':dic, 'context_old':context_old}
        return context

def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST['phone']
        if len(phone) < 10 or len(phone) > 10:
            #return HttpResponse("Phone number should have a length of 10")
            raise ValidationError("Phone number should have a length of 10")
        email = request.POST.get('email')
        userQuery = request.POST.get('query')
        print(name + " " + phone + " " + email + " " + userQuery) 
    return render(request, 'firstapp/contactus.html')


def contactus2(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():            # when this gets executed it executes something called cleaned_data
            if len(form.cleaned_data.get('query')) > 10:
                form.add_error('query', "Query length is not right")
                return render(request, 'firstapp/contactus2.html', {'form':form})
            form.save()
            return HttpResponse("Thank you. We will get back to you. ")
        else:
            if len(form.cleaned_data.get('query')) > 10:
                #form.add_error('query', "Query length is not right")
                form.errors['query'] = ['Query length is not right', 'It should be under 10']
            return render(request, 'firstapp/contactus2.html', {'form':form})

    return render(request, 'firstapp/contactus2.html', {'form':ContactUsForm})