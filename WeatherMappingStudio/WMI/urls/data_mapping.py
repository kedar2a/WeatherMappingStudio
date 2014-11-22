from django.conf.urls import patterns, include, url
from WeatherMappingStudio.WMI.views import data_mapping


urlpatterns = patterns('WeatherMappingStudio.WMI.views.data_mapping',
	#url(r'^cluster_json/$', data_mapping.create_cluster_json, name='create_cluster_json'),
	url(r'^live_json/$', data_mapping.create_live_json, name='create_live_json'),
	#url(r'^heatmap_json/$', data_mapping.create_heatmap_json, name='create_heatmap_json'),	
	
	)
