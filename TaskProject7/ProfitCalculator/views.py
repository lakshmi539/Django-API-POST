from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
@method_decorator(csrf_exempt,name='dispatch')
class ProfitView(View):
    def post(self,request):
        data=json.loads(request.body)
        cp=data.get('cost_price')
        sp=data.get('selling_price')
        p= sp - cp    
        result={
                "Cost_price": cp, 
                "Selling_price": sp, 
                "Profit": p
        }
        return JsonResponse(result)
        