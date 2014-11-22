from django.conf.urls.defaults import url
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    '',
    url(r'^data/', include('WeatherMappingStudio.WMI.urls.data_insert',)),
    url(r'^showlive/', include('WeatherMappingStudio.WMI.urls.live_mapping',)),
    url(r'^showcluster/', include('WeatherMappingStudio.WMI.urls.cluster_mapping',)),
    url(r'^showheatmap/', include('WeatherMappingStudio.WMI.urls.heatmap_mapping',)),
    url(r'^showstats/', include('WeatherMappingStudio.WMI.urls.stats',)),
    url(r'^leaflet/', include('WeatherMappingStudio.WMI.urls.page_mapping',)),
    url(r'^page/', include('WeatherMappingStudio.WMI.urls.page_mapping',)),
    )
