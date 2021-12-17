from django.shortcuts import render

from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from pyfcm import FCMNotification


from .forms import SendMessageForm
from .models import DeviceToken
# Create your views here.


SERVER_KEY = "AAAATrqz7Ws:APA91bFpngrnTnE17ermRoJgx1thg-RYman0KQmzgsm9JFSzKExE59RgbbeFmWFRRuKvKwTvu6h2HyJZOTl5WfGZuGUbXiI8te-t0TuL9toopHh8Vr4omBJ5dPTjYBHIkEpall6xZyzW"


@csrf_exempt
def register_token_api(request):
    if request.method == 'POST':
        token = request.POST['token']
        user_id = request.POST['user_id']

        DeviceToken.objects.create(
            token=token,
            user_id=user_id
        )

        return JsonResponse(data={
            'message': 'token ' + token + ' user id ' + user_id
        })
    else:
        return JsonResponse(data={
            'message': 'Request GET'
        })


def send_message_view(request):
    if request.method == 'GET':
        form = SendMessageForm()

        return render(request=request, template_name='send_message_form.html', context={
            'form': form
        })
    else:
        form = SendMessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            user_id = form.cleaned_data['user_id']


            device_token = DeviceToken.objects.get(user_id=user_id)

            push_notification = FCMNotification(api_key=SERVER_KEY)

            result = push_notification.notify_single_device(registration_id=device_token.token,message_body=message, message_title=title)


            return JsonResponse(data={
                'title' : title,
                'message': message,
                'result' : result
            })
        return JsonResponse(data={
            'message' : 'Error'
        })