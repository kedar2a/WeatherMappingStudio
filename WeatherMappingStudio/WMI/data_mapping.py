from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render_to_response
from WeatherMappingStudio.WMI.models import Sender,Data,Location

def create_live_json(request):
	counter=0
	json=""
	if request.method =="GET":
		dt = request.GET['date']
		lat = request.GET['lat']
		lon = request.GET['lon']
		
		data = Data.objects.get(Q(time_stamp = dt))
		
		if data:
			json="["
			for row in data:
				if counter>0:
					json+=","
				temp = row.temprature
				hum = row.humidity
				windvel = row.windvelocity
				
				address = Location.objects.get(Q(latitude = lat), Q(longitude = lon))
				
				json +='{"temp":"' + temp + '","hum":"'+ hum + '","windvel":"'+ windvel + '","address":"'+ address +'"}'
				counter +=1		
			json+="]"
			
	json+=""
  	t = get_template('live_leaflet.html')
	html = t.render(RequestContext(request,json))	
	return HttpResponse(json)
	

def create_heatmap_json(request):
		
	return HttpResponse('File Created')


	
def create_cluster_json(request):
	data = Data.objects.all()
	f = open('WMI/templates/WMI.json','w') 
	for d in data:	
		temp = str(d.temperature)
		humid = str(d.humidity)
		windvel = str(d.windvelocity)
		#mno = str(d.sender)
		str_data = '{"temperature":' + temp + ',"humidity":' + humid + ',"windvelocity":' + windvel '}'
		f.write(str_data)	
	
	f.close()
	return HttpResponse('File Created')
