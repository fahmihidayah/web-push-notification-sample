from django.views import generic
from django.shortcuts import render
from django.http.response import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class AddDeviceView(generic.View):

    def get(self, request):
        return JsonResponse(
            data={
                'message' : 'ok'
            }
        )

    def post(self, request):
        return JsonResponse(data={
            'name' : 'Test'
        })