from django.shortcuts import render

# Create your views here.
# from django.http import JsonResponse

from django.shortcuts import render
from django.views.generic import View
from django.db.models import Count

from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response

from chartjs.models import SparkData

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'chartjs/index.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        qs = SparkData.objects.filter(status="DELIEVERED").values("location").distinct().annotate(total=Count("pk"))
        labels = list()
        chartdata = list()
        for val in qs:
            labels.append(val.get("location"))
            chartdata.append(val.get("total"))
        chartLabel = "Orders Delievered per location"
        data = dict(
            labels=labels,
            chartLabel=chartLabel,
            chartdata=chartdata
        )
        return Response(data)
