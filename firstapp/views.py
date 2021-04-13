from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, FormView
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy

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


def contactus2(request):                #contact us function based view
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():            # when this gets executed it executes cleaned_data
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

class ContactUs(FormView):          # contact us class based view
    form_class = ContactUsForm
    template_name = 'firstapp/contactus2.html'
    success_url = reverse_lazy("firstapp:index")

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """

        if len(form.cleaned_data.get('query')) > 10:
            form.add_error('query', "Query length is not right")
            return render(self.request, 'firstapp/contactus2.html', {'form':form})
        form.save()
        response = super().form_valid(form)
        return response
    
    def form_invalid(self, form):
        """
        If the form is invalid, render the invalid form.
        """
        if len(form.cleaned_data.get('query')) > 10:
            form.add_error('query', "Query length is not right")
            #form.errors['query'] = ['Query length should be under 10']
        response = super().form_invalid(form)
        return response

