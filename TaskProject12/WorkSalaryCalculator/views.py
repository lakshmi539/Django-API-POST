from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
@method_decorator(csrf_exempt,name='dispatch')
class WorkView(View):
    def post(self,request):
        data=json.loads(request.body)
        hw=data.get('hours_worked')
        rg=data.get('regular_hours')
        hr=data.get('hourly_rate')
        ov=data.get('overtime_rate')
        rp = rg * hr 
        oh = hw - rg 
        op = oh * ov 
        ts = rp + op          
        result={
            "hours_worked": hw, 
            "regular_hours": rg, 
            "hourly_rate": hr, 
            "overtime_rate": ov, 
            "regular_pay": rp, 
            "overtime_hours": oh, 
            "overtime_pay": op, 
            "total_salary": ts                     
        }
        return JsonResponse(result)