# FarmSetu

Implementation:

Developed a API to parse summarised weather data from UK MetOffice.

Two ways implemented to parse data:
1. Pandas Data Frame (comment the access in Service Repo(get_report_service.py))
2. Hard Coded (directly send the data in the form of json)

endpoint: "api/weather/get-report"
method: "POST"
request parameter: {
    "region":"UK",
    "parameter":"Tmax"
}

valid options for region: All valid region provided by UK MetOffice.
valid options for parameter: All valid parameter provided by UK MetOffice.



curl:

curl --location --request POST 'http://127.0.0.1:8000/api/weather/get-report' \
--header 'Content-Type: application/json' \
--data-raw '{
    "region":"UK",
    "parameter":"Tmax"
}'
