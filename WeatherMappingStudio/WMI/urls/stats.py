from django.conf.urls import patterns, include, url
from WeatherMappingStudio.WMI.views import stats


urlpatterns = patterns('WeatherMappingStudio.WMI.views.stats',
	url(r'^dailyjson/$', stats.create_hourly_json, name='create_hourly_json'),
	
	)
