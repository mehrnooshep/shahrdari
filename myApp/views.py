# Create your views here.
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
	#request.get['username']
	#request.post
	#l = SaleBill.objects.all()[0]
	#return HttpResponse('{0} and {1} and {2}'.format(l.saleDate, l.totalPrice, l.costumer.balance))
	return render(request, 'show_table.html', {})

def table_data(request):

	try:
		page = int(request.GET['page'])
	except:
		page = 1
	try:
		rowcount = int(request.GET['rows'])
	except:
		rowcount = 20

	data = RollCall.objects.all()[(page-1)*rowcount: (page)*rowcount];
	jdata = {"total":len(data), "page":page, "records":rowcount, "rows":[]}
	
	for rc in data:
		row = {}
		row['date'] = unicode(rc.date)
		row['entrance'] = unicode(rc.entrance_time)
		row['exit'] = unicode(rc.exit_time)
		jdata['rows'].append(row)
	return HttpResponse(json.dumps(jdata), content_type="application/json")

