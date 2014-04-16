from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader	

# Create your views here.
def index(request):
	#return HttpResponse("Hello, world. You're at the poll index.")
	#import urllib2
	#json_get = urllib2.urlopen("http://localhost:8000/snippets/.json")
	#json_get = urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=8-10%20Broadway,%20London%20SW1H%200BG,%20United%20Kingdom&sensor=false")
	#import json
	#json_obj = json.loads(json_get)
	import json
	import urllib2
	import os
	j = urllib2.urlopen("http://sleepy-plateau-3929.herokuapp.com/snippets/.json")
	js = json.load(j)
	outputT = "<br>"
	'''
	normally get json object is <list> or <unicode> string
	it need decode to big5 if you want to operate with "string" in big5 system
	'''

	for rs in js:
		outputT += rs['code'].decode('big5')
		outputT += "<br>"
	context = {'snippets_list': js}
	'''
	Note: the set template path will back to project default, not relative path.
	('/Users/Evan/Documents/heroku/rest_all/tutorial/templates',)
	http://stackoverflow.com/questions/1926049/django-templatedoesnotexist
	'''
	#PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
	#TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)
	#print TEMPLATE_DIRS
	#template = loader.get_template('webs/index.html')
	#print TEMPLATE_DIRS
	#print template
	#return HttpResponse(template.render(context))
	return render(request, 'webs/index.html', context) 
	#return HttpResponse(outputT)

	#template = loader.get_template('webs/index.html')
	