from django.conf.urls import patterns, include, url
from WeatherMappingStudio.WMI.views import heatmap_mapping


urlpatterns = patterns('WeatherMappingStudio.WMI.views.heatmap_mapping',
	url(r'^json/$', heatmap_mapping.create_json, name='create_json'),
	#url(r'^humidity_json/$', heatmap_mapping.create_humidity_json, name='create_humidity_json'),
	#url(r'^wind_json/$', heatmap_mapping.create_wind_json, name='create_wind_json'),	
	
	)
