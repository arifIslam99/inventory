from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def index(request):
#     return HttpResponse("Allahu Akbar")
def index(request):
        template=loader.get_template('index.html')
        return HttpResponse(template.render())
def staff(request):
        return render(request, 'contents/staff.html')
def products(request):
        return render(request, 'contents/products.html')
def orders(request):
        return render(request, 'contents/orders.html')
def profile(request):
        return render(request, 'contents/profile.html')
