from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from weather_api.service.get_report_service import GetReportService
report_service = GetReportService()


class GetReportController(APIView):
	def post(self, request):
		# get result
		result = report_service.get_formated_data(request)
		return Response(result, status="200")