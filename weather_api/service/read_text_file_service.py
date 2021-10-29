import pandas as pd

class ReadTextFileService:
	def get_data_frame(self, data):
		columns = []
		all_data = []
		for d in data.split("\n"):
			if len(d) != 0:
				# build column
				if columns==[]:
					if d[:4]=="year":
						columns = purifyString(d)

				if d[0].isdigit():
					all_data.append(purifyString(d))

		df = self.build_data_frame(all_data, columns)
		return df.to_json()

	def build_data_frame(self, all_data, columns):
		df = pd.DataFrame(all_data, columns=columns)
		return df

	def get_simple_data(self, data):
		columns = []
		all_data = []
		for d in data.split("\n"):
			if len(d) != 0:
				# build column
				if columns==[]:
					if d[:4]=="year":
						columns = purifyString(d)

				# append data related to column
				if d[0].isdigit():
					if columns!=[]:
						all_data.append(purifyString(d, columns))
		
		result = {}
		result["columns"]=columns
		result["data"]=all_data
		return result

# to handle None value and other unwanted values
def purifyString(str_data, columns=[]):
	result = [None if s=="---" else s for s in str_data.split(" ") if s!=""]
	if len(columns)<1:
		return result
	result = dict(zip(columns, result))
	return result

