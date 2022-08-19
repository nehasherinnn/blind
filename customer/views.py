from django.shortcuts import render

# Create your views here.

def cart (request):
    return render(request,"customer/cart.html")
def item (request):
    return render(request,"customer/items.html")