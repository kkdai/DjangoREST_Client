from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader	

# Create your views here.
def index(request):
	import json
	import urllib2
	import os
	'''
	Using real domain address avoid for server connection.
	'''
	j = urllib2.urlopen("http://sleepy-plateau-3929.herokuapp.com/snippets/.json")
	js = json.load(j)
	outputT = "<br>"
	'''
	normally get json object is <list> or <unicode> string
	it need decode to big5 if you want to operate with "string" in big5 system
	'''
	#for rs in js:
	#	outputT += rs['code'].decode('big5')
	#	outputT += "<br>"
	print outputT  #print for debugging using.
	context = {'snippets_list': js}
	return render(request, 'webs/index.html', context) 

def detail(request, snippet_id):
	import json
	import urllib2
	import os
	jsonUrl = "http://sleepy-plateau-3929.herokuapp.com/snippets/" + str(snippet_id) + "/.json"
	#print jsonUrl
	j = urllib2.urlopen(jsonUrl)
	js = json.load(j)
	print js
	context = {'snippet':js, 'detail_url':jsonUrl}
	print type(context)
	return render(request, 'webs/detail.html', context)
