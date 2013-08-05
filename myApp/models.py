# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.
class RollCall(models.Model):
	date = models.DateField(auto_now_add=True, verbose_name=u"تاریخ")
	entrance_time = models.DateField(auto_now_add=True, verbose_name=u"زمان ورود")
	exit_time = models.DateField(auto_now_add=True, verbose_name=u"زمان خروج")
