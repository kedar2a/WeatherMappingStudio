from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import RequestContext,Template
from django.template.loader import get_template
from django.shortcuts import render_to_response

from datetime import datetime, timedelta
from WeatherMappingStudio.WMI.models import Sender,Data,Location

import json

@csrf_exempt
def create_json(request):
	#the_dump = ""
	json = ""
	date = ""
	counter = 0
	var = ""
	vardata = ""
	datetime = ""

	if request.method =="GET":
		var = request.GET['rbtvalue']
		datetime = request.GET['time_stamp']
	
	# for a given time for all lat | lon 	
	if datetime:
		time_threshold_less = datetime - timedelta(minutes=30)
		time_threshold_more = datetime + timedelta(minutes=30)
		data = Data.objects.filter(time_stamp_gt = time_threshold_less, time_stamp_lte = time_threshold_more)
	
	# for latest update from database			
	else:
		data = Data.objects.latest()
		
	datetime = data.time_stamp	
	
	data_queryset = Data.objects.filter(time_stamp = datetime)	
	json = '{ \n\t"time_stamp": "' + str(datetime) + '", "values" : \n\t['
	for rows in data_queryset:
		if var=="Temperature":	
			vardata = rows.temperature
		if var=="Humidity":	
			vardata = rows.humidity
		if var=="Wind Velocity":	
			vardata = rows.windvelocity	
		loc_id = rows.location_id
		
		location = Location.objects.get(id = loc_id)
			
		if counter > 0 :
			 json += ','
		json += '\n\t\t{"address" : "' + location.address + '",'	 
		json += '"latitude" : "' + str(location.latitude) + '",'
		json += '"longitude" : "' + str(location.longitude) + '",'
		json += '"value" : "' + str(vardata) + '"}'
		counter += 1
		
	json += '\n\t]\n}'	
		
		#json1={}
		#json1["address"] = location.address
		#json1["latitude"] = location.latitude
		#json1["longitude"] = location.longitude
		#json1[var] = vardata
		#the_dump+=json.dumps(json1)
	#print "json data : ",json
	return HttpResponse(json)
