from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
@method_decorator(csrf_exempt,name='dispatch')
class DiscountView(View):
    def post(self,request):
        data=json.loads(request.body)
        p=data.get('price')
        d=data.get('discount_percentage')
        damt =(p * d) / 100 
        fp = p - d       
        result={
                "Price": p, 
                "Discount_percentage": d, 
                "Discount_amount": damt, 
                "Final_price": fp
            }
        return JsonResponse(result)