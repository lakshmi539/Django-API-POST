from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
@method_decorator(csrf_exempt,name='dispatch')
class SimpleInterestView(View):
    def post(self,request):
        data=json.loads(request.body)
        p=data.get('principal')
        r=data.get('rate')
        t=data.get('time')
        si=(p*r*t)/100
        result={
            "Principal":10000,
            "Rate":5,
            "Time":2,
            "Simple-Interest":si
        }
        return JsonResponse(result)