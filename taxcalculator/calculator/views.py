from django.http import HttpResponse
from django.shortcuts import render


tax_rate=0.15
# Create your views here.
def index(request):
    return HttpResponse("<h1>  this is a site to calculate tax <h1>")

def calculate_tax(request,amount):
    total=float(amount)*(1+tax_rate)
     return HttpResponse(f"<h1> total price after tax{total:.2f}<h1>")

def show(request):
    return HttpResponse(f"<h1> the current tax {tax_rate*100}% <h1>")
