from django.conf.urls import patterns, include, url
from WeatherMappingStudio.WMI.views import page_mapping


urlpatterns = patterns('WeatherMappingStudio.WMI.views.page_mapping',
	url(r'^live/$', page_mapping.liveleaflet_view, name='liveleaflet_view'),
	url(r'^cluster/$', page_mapping.clusterleaflet_view, name='clusterleaflet_view'),
	url(r'^heatmap/$', page_mapping.heatmap_view, name='heatmap_view'),
	url(r'^inputpage/$', page_mapping.input_view, name='input_view'),
	)
