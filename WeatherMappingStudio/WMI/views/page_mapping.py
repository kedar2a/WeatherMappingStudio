from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Template, RequestContext

def clusterleaflet_view(request):
	return render_to_response('cluster_leaflet.html')
	
def liveleaflet_view(request):
	return render_to_response('live_leaflet.html')
	
def heatmap_view(request):
	return render_to_response('heatmap_leaflet.html')
	
def input_view(request):
	return render_to_response('input.html')
