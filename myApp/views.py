#-*- encoding:utf-8 -*-
# Create your views here.
import mimetypes
from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import *
import json

def index(request):
	#request.get['username']
	#request.post
	#l = SaleBill.objects.all()[0]
	#return HttpResponse('{0} and {1} and {2}'.format(l.saleDate, l.totalPrice, l.costumer.balance))
	print "hellooooo"
	return render(request, 'mybase.html', {})
def show_table(request):
	#request.post
	#l = SaleBill.objects.all()[0]
	#return HttpResponse('{0} and {1} and {2}'.format(l.saleDate, l.totalPrice, l.costumer.balance))
	return render(request, 'show_table.html', {})

def table_data(request, filter_id):

	filter_id = int(filter_id)
	try:
		page = int(request.GET['page'])
	except:
		page = 1
	try:
		rowcount = int(request.GET['rows'])
	except:
		rowcount = 20
	print filter_id
	data =[]
	if filter_id ==1 :
		print "here"
		data = ETL.objects.filter(subsystemName = '137')[(page-1)*rowcount: (page)*rowcount];
		# if etls.subsystemName == '137':
		# 	etls.filterId=1
		# elif self.subsystemName == '1888':
		# 	self.filterId=2
		# elif self.subsystemName == 'آموزش':
		# 	self.filterId=3
		# elif self.subsystemName == 'ارزشیابی کارکنان':
		# 	self.filterId=4
		# elif self.subsystemName == 'ارزشیابی مدیران':
		# 	self.filterId=5
		# elif self.subsystemName == 'ارزشیابی عملکرد مناطق':
		# 	self.filterId=6
		# elif self.subsystemName == 'عوارض خودرو':
		# 	self.filterId=7

	# print(data.count())
	jdata = {"total":len(data), "page":page, "records":rowcount, "rows":[]}
	print "beforee"
	# print(data.get(id=2).id)
	for rc in data:
		print ("forrrr")
		row = {}
		row['name'] = unicode(rc.subsystemName)
		row['ETLStart'] = unicode(rc.ETLStart)
		row['ETLEnd'] = unicode(rc.ETLEnd)
		row['ETLSuccess'] = unicode(rc.ETLSuccess)
		row['SSASStart'] = unicode(rc.SSASStart)
		row['SSASEnd'] = unicode(rc.SSASEnd)
		row['SSASSuccess'] = unicode(rc.SSASSuccess)
		jdata['rows'].append(row)
		print rc.id

	return HttpResponse(json.dumps(jdata), content_type="application/json")


