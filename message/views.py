from django.shortcuts import render,render_to_response
from aboutme.models import Myself

def showmessage(request):
    myself = Myself.objects.all();
    if len(myself) > 0:
        return render(request, 'message.html', {'myselfInfo': myself[0]})
    return render(request, 'message.html')