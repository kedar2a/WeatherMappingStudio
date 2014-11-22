from django.db import models

class Sender(models.Model):
	#username = models.CharField(max_length=50)
	#password = models.CharField(_('password'), max_length=128, help_text=_("Use'[algo]$[salt]$[hexdigest]' or use the <a href=\"password/\">change password form</a>."))
	name = models.CharField(max_length=50)
	number = models.PositiveIntegerField(unique=True)

	def __unicode__(self):
        	return u"%s %s" % (self.name, self.number)

	#def set_password(self, raw_password):
    	#	import random
    	#	algo = 'sha1'
    	#	salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
    	#	hsh = get_hexdigest(algo, salt, raw_password)
    	#	self.password = '%s$%s$%s' % (algo, salt, hsh)
        	
class Location(models.Model):
	
	latitude = models.DecimalField(max_digits=10, decimal_places=6)
	longitude = models.DecimalField(max_digits=10, decimal_places=6)
	address = models.TextField()	
	
	
	unique_together = ("latitude", "longitude")
	
	def __unicode__(self):
        	return u"%s %s %s" % (self.latitude, self.longitude, self.address)	

        	
class Data(models.Model):
	temperature = models.DecimalField(max_digits=5, decimal_places=2)
	humidity = models.DecimalField(max_digits=5, decimal_places=2)
	windvelocity = models.DecimalField(max_digits=5, decimal_places=2)
	#winddirection NOT INCLUDED RIGHT NOW COZ WE DIDN'T KNEW THE FORMAT OF INPUT
	time_stamp = models.DateTimeField()
	sender = models.ForeignKey(Sender, null=True,blank=True)
	location = models.ForeignKey(Location)
	
	class Meta:
      		get_latest_by = 'time_stamp'
	
	def __unicode__(self):
        	return u"%s %s %s %s %s %s" % (self.sender, self.temperature, self.humidity, self.windvelocity, self.location, self.time_stamp)
