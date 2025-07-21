from django.shortcuts import render
from . models import Concat
from django.http import HttpResponse

def concat_view(request):
    return render(request, 'concat/view.html')

def save_concat(request):
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        concat = Concat(
            name = name,
            email = email,
            phone_number = phone_number,
            subject = subject,
            message = message
        )

        concat.save()
        return HttpResponse('OK', content_type='text/plain')
    except:
        return HttpResponse('저장 실패', content_type='text/plain')
