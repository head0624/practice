from django.shortcuts import render

def price_view(request):
    return render(request, 'price/view.html')