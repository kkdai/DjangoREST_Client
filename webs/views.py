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
	number_count = len(js)
	'''
	normally get json object is <list> or <unicode> string
	it need decode to big5 if you want to operate with "string" in big5 system
	'''
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
	'''
	For multiple context, it could be input as follow.
	'''
	context = {'snippet':js, 'detail_url':jsonUrl}
	print type(context)
	return render(request, 'webs/detail.html', context)

def form(request):
	import json
	import urllib2
	import os
	j = urllib2.urlopen("http://sleepy-plateau-3929.herokuapp.com/snippets/.json")
	js = json.load(j)
	number_count = str(len(js))
	print number_count
	context = {'snippet_count':number_count}
	return render(request, 'webs/form.html', context)

def post_form(request):
	code_string = request.POST['Name']
	print code_string
	return HttpResponse(code_string)

