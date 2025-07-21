from django.shortcuts import render

def home_index(request):
    return render(request, 'home/index.html')

def footer(request):
    return render(request, 'home/footer')