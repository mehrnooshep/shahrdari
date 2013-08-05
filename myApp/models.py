<<<<<<< HEAD
# -*- encoding: utf-8 -*-
=======
#coding=UTF-8
>>>>>>> c0226b0e6f714e8f17a1eb50b83e080f7901b4b6
from django.db import models

# Create your models here.
class RollCall(models.Model):
	date = models.DateField(auto_now_add=True, verbose_name=u"تاریخ")
	entrance_time = models.DateField(auto_now_add=True, verbose_name=u"زمان ورود")
	exit_time = models.DateField(auto_now_add=True, verbose_name=u"زمان خروج")
