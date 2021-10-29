from django.urls import path
from weather_api.controller.get_report_controller import GetReportController

urlpatterns=[
	path('get-report', GetReportController.as_view())
]