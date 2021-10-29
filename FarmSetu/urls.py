from django.contrib import admin
from django.urls import path, include
api_route = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{api_route}/weather/', include('weather_api.urls'))
]
