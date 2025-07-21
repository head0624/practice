from django.shortcuts import render

def features_view(request):
    return render(request, 'features/view.html')
