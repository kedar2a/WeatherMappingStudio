from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Template, RequestContext,Context,loader

def home_view(request):
	#print 'THE ROOT : ',settings.STATIC_ROOT
	#t = loader.get_template('home.html')
   	#c = Context({'STATIC_ROOT': settings.STATIC_ROOT})
   	#return HttpResponse(t.render(c))
	return render_to_response('home.html')

