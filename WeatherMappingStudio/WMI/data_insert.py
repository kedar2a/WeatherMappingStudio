from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.views.decorators.csrf import csrf_exempt
from WeatherMappingStudio.WMI.models import Sender,Data,Location

from decimal import *
import csv
import random

@csrf_exempt
def via_app(request):
	mno = request.GET.get('mno')
	temp = request.GET.get('temp')
	hum = request.GET.get('humidity')
	windvel = request.GET.get('windvelocity')

	print mno,temp,hum,windvel,"printing values"
	sender = Sender(number=int(mno))
	sender.save()

	data = Data(temperature=Decimal(temp), humidity=Decimal(hum), windvelocity=Decimal(windvel), sender_id=sender.number)
	data.save()	
	
	return HttpResponse("Done")
	
	
def through_form(request)

	return HttpResponse("Done")
	
	
def from_csv(request):
	counter = 0
	dt_str = ""
	address_list = []
	lat_list = []
	lon_list = []
	temp_list = []
	dt_list = []
				
	with open('WeatherMappingStudio/WMI/CSV/ARG-2012-01-01.csv')as csvfile:
		 datareader = csv.reader(csvfile, delimiter=',')
		 for row in datareader:
			address_list.append(row[1])
		 	lat_list.append(row[4])
		 	lon_list.append(row[5])
		 	temp_list.append(row[7])
		 	
		 	dt_str = row[2]
		 	date = dt_str[:-9]
		 	i = len(date)+1
		 	str_rem = dt_str[i:]
		 	
		 	month = str_rem[:-5]
			if month == 'jan' or month == 'Jan':
		 		month = '01'
		 	elif month == 'feb' or month == 'Feb':
		 	  	month = '02'
		 	elif month == 'mar' or month == 'Mar':
		 	  	month = '03'
		 	elif month == 'apr' or month == 'Apr':
		 	  	month = '04'
		 	elif month == 'may' or month == 'May':
		 	  	month = '05'
		 	elif month == 'jun' or month == 'june' or month == 'Jun' or month == 'June':
		 	  	month = '06'
		 	elif month == 'jul' or month == 'july' or month == 'Jul' or month == 'July':
		 	  	month = '07'
		 	elif month == 'aug' or month == 'Aug':
		 	  	month = '08'
		 	elif month == 'sep' or month == 'Sep':
		 	  	month = '09'
		 	elif month == 'oct' or month == 'Oct':
		 	  	month = '10'
		 	elif month == 'nov' or month == 'Nov':
		 	  	month = '11'
		 	elif month == 'dec' or month == 'Dec':
		 	  	month = '12'
		 	
		 	year = str_rem[4:]
		 			 	
	                dt_str = year + "-" + month + "-" + date + " " + row[3]
	                dt_list.append(dt_str)
	print lat_list[18], lon_list[18], address_list[18]	
	for i in range(len(lat_list)):
		if counter == 0:
		 	counter += 1
			continue
		counter+=1	
		loc = Location.objects.get_or_create(latitude=Decimal(lat_list[i]),longitude=Decimal(lon_list[i]),address=address_list[i])
		
		if temp_list[i] == " ":
			
			continue
		data = Data(temperature = Decimal(temp_list[i]), humidity = Decimal(random.randrange(45,70,3)), windvelocity = Decimal(random.randrange(3,15,3)), time_stamp = dt_list[i])
		
		data.location = loc[0]		
		data.save()
		
					
	return HttpResponse("Done")

	
#	code for fetching address from lat long
#
#def geocode(data):
#    url_list = []
#    for item in data:
#        address = ('%s+%s' % (item.city, item.country)).replace(' ', '+')
#        url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % address
#        url_list.append([item.pk, url])
#
#    json_results = []
#    for url in url_list:
#        r = requests.get(url[1])
#        json_results.append([url[0], r.json])
#
#    result_list = []
#    for result in json_results:
#        if result[1]['status'] == 'OK':
#            lat = float(result[1]['results'][0]['geometry']['location']['lat'])
#            lng = float(result[1]['results'][0]['geometry']['location']['lng'])
#            marathon = Marathon.objects.get(pk=result[0])
#            marathon.point = GEOSGeometry('POINT(%s %s)' % (lng, lat))
#            marathon.save()
#
#    return result_list
	
