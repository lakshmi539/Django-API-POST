from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
@method_decorator(csrf_exempt,name='dispatch')
class ElectricityBillView(View):
    def post(self,request):
        data=json.loads(request.body)
        u=data.get('units')
        r=data.get('rate')
        bill=u*r
        result={
            "Units":u,
            "Rate":r,
            "Bill-Amount":bill
        }
        return JsonResponse(result)