from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import RequestContext,Template
from django.template.loader import get_template
from django.shortcuts import render_to_response

from WeatherMappingStudio.WMI.models import Sender,Data,Location

import json

@csrf_exempt	
def create_live_json(request):
	counter = 0
	#json = ""
	temp = ""
	hum = ""
	windvel= ""
	loc_id = ""
	#time_stamp = ""
	
	if request.method =="POST":
		lat=request.POST['lat']
		lon=request.POST['lng']
		
		loc_queryset = Location.objects.filter(latitude__startswith=lat,longitude__startswith=lon)
		#print "Loc Qset count :",loc_queryset.count()	
		if loc_queryset:
			#print "loc yes"
			loc = Location.objects.get(latitude__exact=lat,longitude__exact=lon)
		        address = str(loc.address)
		        loc_id = loc.id
		        #print "latitude : ",loc.latitude, " longitude : ",loc.longitude	
		        #print "address ; ",address, " location id : ",loc.id
		        data_queryset = Data.objects.filter(location__exact=loc_id)
		        #for each in data_queryset:
		        #	print "tuple : ",each 
		        #print "Data Qset :",data_queryset.latest()
			#print "Data Qset count :",data_queryset.count()
			d = data_queryset.latest()
			if d:
				#print "data yes"
				temp = str(d.temperature)
				hum = str(d.humidity)
				windvel = str(d.windvelocity)
				#time_stamp = str(d.time_stamp)
			else:
			 	temp = ""
				hum = ""
				windvel = ""        	
		else:
			address = ""	

	#	json in string format	
	#	json = '{"address":"' + address + '","temperature":"'+ temp + ,'"humidity":"'+ hum + ,'"windvelocity":"'+ windvel + '"}'
		
	#	json as a dict
		json1={}
		json1["loc_id"]=loc_id
		json1["address"]=address
		json1["temperature"]=temp
		json1["humidity"]=hum
		json1["windvelocity"]=windvel
		#json1["time_stamp"]=time_stamp[:-15]
		the_dump=json.dumps(json1)
	#	print json1
  	#t = get_template('live_leaflet.html')
	#html = t.render(RequestContext(request,json))
	return HttpResponse(the_dump)
	

