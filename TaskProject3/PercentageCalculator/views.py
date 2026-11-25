from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@method_decorator(csrf_exempt, name="dispatch")
class PercentageView(View):
    def post(self, request):
        data = json.loads(request.body)
        b = data.get("birth_year")
        c = data.get("current_year")
        age = c - b
        result = {"Age": age}
        return JsonResponse(result)
