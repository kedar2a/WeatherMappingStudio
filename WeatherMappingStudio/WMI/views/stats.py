from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import RequestContext,Template
from django.template.loader import get_template
from django.shortcuts import render_to_response

from datetime import datetime, timedelta
from WeatherMappingStudio.WMI.models import Sender,Data,Location

import json
import dateutil.parser

@csrf_exempt
def create_hourly_json(request):

	loc_id = ""
	json = ""
	counter = 0
	time = 0
	
	dataset_dt = ""
	start_dt = ""
	curr_dt = ""
	pre_dt = ""
	
	temp = ""
	hum = ""
	windvel =""
	letter = 'A'

	if request.method =="GET":
		loc_id = request.GET['locId']
		option = request.GET['period']
		
	print 'OPTION :',option	
		
	if loc_id:
		location_obj = Location.objects.get(id = loc_id)
		data_set = Data.objects.filter(location = loc_id)
		data = data_set.latest()
		timestamp = data.time_stamp
		data_query_set = Data.objects.filter(location = loc_id)#.distinct('time_stamp')
		start_dt = timestamp
		
	else :
		return HttpResponse("Location not registered") 
	
	
	if (option == 'Daily'):
		time = 24
	elif(option == 'Weekly'):
		time = 7
	elif (option == 'Monthly'):
		time = int(start_dt.day)
	elif (option == 'ThirtyDays'):
		time = 30
		
	#for last 24 records
	#result = data_query_set.order_by('time_stamp').reverse()[:24]
	
	
	
	#for last 24hrs new
	if option == 'Daily':
		json +='['
	
		for i in range(time):
			if (counter>0):
				json += ","
			curr_dt = start_dt - timedelta(hours=i)
			hour_query_set = data_query_set.filter(time_stamp = curr_dt)

			hour = str(curr_dt.hour)	
			
			if hour_query_set:
				tot_temp = 0
				tot_hum = 0
				tot_windvel = 0

				for rows in hour_query_set:
					tot_temp += rows.temperature
					tot_hum += rows.humidity
					tot_windvel += rows.windvelocity
	
				length = len(hour_query_set)
				temp = str(round(tot_temp/length,2))
				hum = str(round(tot_hum/length,2))
				windvel = str(round(tot_windvel/length,2))
	
				json +='\n{"period":' + hour + ', "temp":' + temp + ', "hum":' + hum + ', "windvel":' + windvel + '}'
	
			else:
				json +='\n{"period":' + hour + ', "temp":"", "hum":"", "windvel":""}'	
	
			counter += 1
		
		json += '\n]'
	
	else:
	
		#for past week / current month / past 30 days
	
		json +='[\n'
	
		for i in range(time):
			if (counter>0):
				json += ","
			curr_dt = start_dt - timedelta(days=i)
			day_query_set = data_query_set.filter(time_stamp__year = curr_dt.year, time_stamp__month = curr_dt.month, time_stamp__day = curr_dt.day)
	
			day = str(curr_dt.day)		
			if day_query_set:
				tot_temp = 0
				tot_hum = 0
				tot_windvel = 0
				length = len(day_query_set) 

				for rows in day_query_set:
					tot_temp += rows.temperature
					tot_hum += rows.humidity
					tot_windvel += rows.windvelocity
	
				temp = str(round(tot_temp/length,2))
				hum = str(round(tot_hum/length,2))
				windvel = str(round(tot_windvel/length,2))
	
				json +='\n{"period":' + day + ', "temp":' + temp + ', "hum":' + hum + ', "windvel":' + windvel + '}'
	
			else:
				json +='\n{"period":' + day + ', "temp":"", "hum":"", "windvel":""}'	
	
			counter += 1
		
		json += '\n]'
	
	
	#for last 24 hrs old
	#time_threshold_less = timestamp - timedelta(hours=23)
	#result = data_query_set.order_by('time_stamp').reverse().filter(time_stamp__range=(time_threshold_less,timestamp))
	
	#curr_dt = start_dt
		
	#json +='['
	#for rows in result:
		#if (counter>0):
		#	json += ","
		
		#extracting data for passing
	#	dataset_dt = rows.time_stamp
	#	temp = str(rows.temperature)
	#	hum = str(rows.humidity)
	#	windvel = str(rows.windvelocity)	
		
		#for repeating values
	#	if(counter>0 and dataset_dt == pre_dt):
	#		continue
		
		#for matching hour count
	#	if(dataset_dt == curr_dt):
	#		json +=	'\n{"hrs":' + str(dataset_dt.hour) + ', "temp":' + temp + ', "hum":' + hum + ', "windvel":' + windvel +', "letter":"' + chr(ord(letter) + counter) + '"}'
	#		if (chr(ord(letter) + counter) != 'X'):
	#			json += ','
		
	#	elif(dataset_dt < curr_dt):
	#		while(dataset_dt < curr_dt):
	#			json +=	'\n{"hrs":' + str(curr_dt.hour) + ', "temp":"", "hum":"" , "windvel":"", "letter":"' + chr(ord(letter) + counter) + '"}'
	#			if (chr(ord(letter) + counter) != 'X'):
	#				json += ','
				
	#			counter += 1
	#			curr_dt -= timedelta(hours=1)
				
	#		if(dataset_dt == curr_dt):
	#			json +=	'\n{"hrs":' + str(dataset_dt.hour) + ', "temp":' + temp + ', "hum":' + hum + ', "windvel":' + windvel +', "letter":"' + chr(ord(letter) + counter) + '"}'
	#			if (chr(ord(letter) + counter) != 'X'):
	#				json += ','
					
	#	else:
	#		json +=	'\n{"hrs":' + str(curr_dt.hour) + ', "temp":"", "hum":"" , "windvel":"", "letter":"' + chr(ord(letter) + counter) + '"}'
	#		if (chr(ord(letter) + counter) != 'X'):
	#			json += ','	
			
		#shifting hr_count val to pre_hr_count, incrementing counter and hr_count	
	#	counter += 1
	#	pre_dt = curr_dt
	#	curr_dt -= timedelta(hours=1)
		
	#json += '\n]'
	
	
	
	
	
	return HttpResponse(json)
