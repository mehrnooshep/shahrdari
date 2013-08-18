# -*- encoding: utf-8 -*-
from django.db import models, connection
# Create your models here.

class ETL(models.Model):
	subsystem = models.CharField(max_length=40 )
	subsystemName = models.CharField(max_length=40 )
	ETLStart = models.DateTimeField( null=True)
	ETLEnd = models.DateTimeField( null=True)
	ETLSuccess = models.BooleanField(default=False)
	SSASStart = models.DateTimeField( null=True)
	SSASEnd = models.DateTimeField( null=True)
	SSASSuccess = models.BooleanField(default=False)
	# filterId= models.IntegerField()

	# def save(self, *args, **kwargs):
	# 	self.filterId = self.set_filter_id()
	# 	return super(ETL, self).save(*args, **kwargs)

	# def set_filter_id(self):
	# 	if self.subsystemName == '137':
	# 		 self.filterId=1
	# 	elif self.subsystemName == '1888':
	# 		self.filterId=2
	# 	elif self.subsystemName == 'آموزش':
	# 		self.filterId=3
	# 	elif self.subsystemName == 'ارزشیابی کارکنان':
	# 		self.filterId=4
	# 	elif self.subsystemName == 'ارزشیابی مدیران':
	# 		self.filterId=5
	# 	elif self.subsystemName == 'ارزشیابی عملکرد مناطق':
	# 		self.filterId=6
	# 	elif self.subsystemName == 'عوارض خودرو':
	# 		self.filterId=7
	# 	elif self.subsystemName == 'فنی-عمرانی':
	# 		self.filterId=8

	def gregorian_to_persian(self, date):
		cursor = connection.cursor
		try:
			cursor.callproc("[dbo].[GregorianToPersian]" ,[str(date)])
			return cursor.return_value
		finally:
			cursor.close()
