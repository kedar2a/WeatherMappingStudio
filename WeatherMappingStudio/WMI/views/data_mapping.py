from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from WeatherMappingStudio.WMI.models import Sender,Data,Location

def create_cluster_json(request):
	data = Data.objects.all()
	f = open('WMI/templates/WMI.json','w') 
	for d in data:	
		temp = str(d.temperature)
		humid = str(d.humidity)
		windvel = str(d.windvelocity)
		mno = str(d.sender)
		str_data = '{"temperature":' + temp + ',"humidity":' + humid + ',"windvelocity":' + windvel + ',"sender_no":' + mno +  '}'
		f.write(str_data)	
	
	f.close()
	return HttpResponse('File Created')
	
@csrf_exempt	
def create_live_json(request):
	counter=0
	json=""
	temp=""
	hum=""
	windvel=""
	if request.method =="POST":
		lat=request.POST['lat']
		lon=request.POST['lng']
		
		print "lat / lon : ",lat,lon
		
		loc_queryset = Location.objects.filter(latitude__startswith=lat,longitude__startswith=lon)
				
		if loc_queryset:
			print "loc true"
			loc = Location.objects.get(latitude__startswith=lat,longitude__startswith=lon)
		        address = str(loc.address)
		        loc_id = loc.id
			data = Data.objects.filter(location=loc_id)
			print "address : ",address,"loc id : ",loc_id, "count : ", data.count()
			if data.count():
				d = Data.objects.get(location__exact=loc_id)
				print "data true"	
				temp = str(d.temperature)
				hum = str(d.humidity)
				windvel = str(d.windvelocity)
			else:
			 	print "data false"
				temp = 'null'
				hum = 'null'
				windvel = 'null'        	
		else:
			address = 'null'	
		
		print "T : ",temp," H : ",hum," W : ",windvel
	#	json = '{"address":"' + address + '","temperature":"'+ temp + ,'"humidity":"'+ hum + ,'"windvelocity":"'+ windvel + '"}'
		json={}
		json["address"]=address
		json["temperature"]=temp
		json["humidity"]=hum
		json["windvelocity"]=windvel
			
  	#t = get_template('live_leaflet.html')
	#html = t.render(RequestContext(request,json))
	return HttpResponse(json)
	
	
def create_heatmap_json(request):
	counter=0
	json=""
	if request.method =="GET":
		lat=request.GET['lat']
		lon=request.GET['lng']
		
		loc = Location.objects.get(latitude=lat,longitude=lon)
		data = Data.objects.get(location=loc.id)
				
		if data:
			json="["
			for obj in queryset:
				if counter>0:
					json+=","
				
				json +='{"address":"' + obj.title + '","url":"'+ url + '"}'
				counter +=1		
			json+="]"
			
	json+=""
  	t = get_template('live_leaflet.html')
	html = t.render(RequestContext(request,json))
	return HttpResponse(json)
