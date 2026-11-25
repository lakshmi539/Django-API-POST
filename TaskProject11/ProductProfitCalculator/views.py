from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
@method_decorator(csrf_exempt,name='dispatch')
class ProductView(View):
    def post(self,request):
        data=json.loads(request.body)
        cp=data.get('cost_price')
        sp=data.get('selling_price')
        q=data.get('quantity')
        tc= cp * q
        ts=sp*q
        p=ts-tc   
        result={
            "cost_price": cp, 
            "selling_price": sp, 
            "quantity": q, 
            "total_cost": tc, 
            "total_sales": ts, 
            "profit": p                     
        }
        return JsonResponse(result)