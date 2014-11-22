from django.conf.urls import patterns, include, url
from WMI import view
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    	(r'^$', 'django.views.generic.simple.redirect_to',{'url': '/home/'}),
        url(r'^home/', view.home_view),
        url(r'^show/', include('WeatherMappingStudio.WMI.urls')),
        url(r'^inserting/', include('WeatherMappingStudio.WMI.urls')),
        url(r'^visualizing/', include('WeatherMappingStudio.WMI.urls')),
        
        #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'STATIC_ROOT'})
        
)
