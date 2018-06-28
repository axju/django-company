from django.shortcuts import render

# Create your views here.

def page(request, name):
    return render(request, 'company/pages/{}.html'.format(name))
