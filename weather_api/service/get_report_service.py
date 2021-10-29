import requests

from weather_api.service.read_text_file_service import ReadTextFileService 
read_text_file_service = ReadTextFileService()

class GetReportService:
	def get_formated_data(self, request):
		region = request.data.get('region')
		parameter = request.data.get('parameter')

		if region==None:
			region = "UK"
		if parameter==None:
			parameter = "Tmax"

		# get text file from api
		data = requests.get(f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter}/date/{region}.txt")
		
		# get data frame
		# result = read_text_file_service.get_data_frame(data.text)

		# simple data
		result = read_text_file_service.get_simple_data(data.text)
		return result