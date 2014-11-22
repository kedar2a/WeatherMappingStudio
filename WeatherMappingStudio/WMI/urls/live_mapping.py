from django.conf.urls import patterns, include, url
from WeatherMappingStudio.WMI.views import live_mapping


urlpatterns = patterns('WeatherMappingStudio.WMI.views.live_mapping',
	url(r'^live_json/$', live_mapping.create_live_json, name='create_live_json'),
	
	)
