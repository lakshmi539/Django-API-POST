from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
@method_decorator(csrf_exempt,name='dispatch')
class AgeView(View):
    def post(self,request):
        data=json.loads(request.body)
        a=data.get('age')
        m = a * 12 
        w = a * 52 
        d = a * 365          
        result={
            "age": a, 
            "months": m, 
            "weeks": w, 
            "days": d              
        }
        return JsonResponse(result)