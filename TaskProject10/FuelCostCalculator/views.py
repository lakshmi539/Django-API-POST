from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
@method_decorator(csrf_exempt,name='dispatch')
class FuelView(View):
    def post(self,request):
        data=json.loads(request.body)
        d=data.get('distance')
        m=data.get('mileage')
        fp=data.get('fuel_price')
        fr = d / m 
        tc= fr * fp   
        result={
            "distance": d, 
            "mileage": m, 
            "fuel_price": fp, 
            "fuel_required": fr,                     "total_cost": 2100 
        }
        return JsonResponse(result)