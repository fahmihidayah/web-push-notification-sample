from django.shortcuts import render, redirect
from .forms import SendMessageForm

# Create your views here.


def send_message_view(request, **kwargs):
    if request.method == 'GET':
        form = SendMessageForm()
        return render(request=request, template_name='send_message.html', context={
            'form' : form
        })
    else:
        form = SendMessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            print('message to be send ' + title + ' ' + message)
        return redirect('send_message')
