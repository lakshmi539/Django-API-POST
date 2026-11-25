from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
@method_decorator(csrf_exempt,name='dispatch')
class TimeView(View):
    def post(self,request):
        data=json.loads(request.body)
        h=data.get('hours')
        m=h*60
        s=h*3600
        result={
            "Hours": h, 
            "Minutes": m, 
            "Seconds": s
        }
        return JsonResponse(result)