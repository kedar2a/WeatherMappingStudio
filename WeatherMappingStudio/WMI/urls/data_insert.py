from django.conf.urls import patterns, include, url
from WeatherMappingStudio.WMI.views import data_insert


urlpatterns = patterns('WeatherMappingStudio.WMI.views.data_insert',
	#url(r'^application/$', data_insert.via_app, name='via_app'),
    	url(r'^csv/$', data_insert.from_csv, name='from_csv'),
    	#url(r'^form/$', data_insert.through_form, name='through_form'),
    	#url(r'^overlay/$', data_insert.through_overlay, name='through_overlay'),
    	
    	)
