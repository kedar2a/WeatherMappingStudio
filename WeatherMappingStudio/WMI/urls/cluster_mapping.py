from django.conf.urls import patterns, include, url
from WeatherMappingStudio.WMI.views import cluster_mapping


urlpatterns = patterns('WeatherMappingStudio.WMI.views.cluster_mapping',
	url(r'^json/$', cluster_mapping.create_json, name='create_json'),
	#url(r'^humidity_json/$', cluster_mapping.create_humidity_json, name='create_humidity_json'),
	#url(r'^wind_json/$', cluster_mapping.create_wind_json, name='create_wind_json'),	
	
	)
