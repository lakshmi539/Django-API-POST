from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
@method_decorator(csrf_exempt,name='dispatch')
class SalaryView(View):
    def post(self,request):
        data=json.loads(request.body)
        bs=data.get('basic_salary')
        b=data.get('bonus')
        d=data.get('deduction')
        ns = bs + b - d
        result={
            "Basic_salary": bs, 
            "Bonus": b, 
            "Deduction": d, 
            "Net_salary": ns
        }
        return JsonResponse(result)