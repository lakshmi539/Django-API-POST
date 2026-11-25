from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
@method_decorator(csrf_exempt,name='dispatch')
class AgeView(View):
    def post(self,request):
        data=json.loads(request.body)
        m=data.get('obtained_marks')
        t=data.get('total_marks')
        p=(m/t)*100
        result={
            "Percentage":p
        }
        return JsonResponse(result)