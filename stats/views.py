from django.shortcuts import render

def stats_view(request):
    return render(request, 'stats/view')