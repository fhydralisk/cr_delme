# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


def gps_field():
    return models.DecimalField(max_digits=9, decimal_places=6)


class Image(models.Model):
    ImageFile = models.ImageField()
    IWidth = models.IntegerField()
    IHeigth = models.IntegerField()
    ILongitude = gps_field()
    ILatitude = gps_field()
    ILongitude2 = gps_field()
    ILatitude2 = gps_field()


class ControlPoint(models.Model):
    CPContinent = models.CharField(max_length=6, null=True, blank=True)
    CPState = models.CharField(max_length=15, null=True, blank=True)
    CPProvince = models.CharField(max_length=15, null=True, blank=True)
    CPID = models.CharField(max_length=20, primary_key=True)
    CPName = models.CharField(max_length=15, null=True, blank=True)
    CPNumber = models.CharField(max_length=15)
    CPType = models.CharField(max_length=16, null=True, blank=True)
    CPGrade = models.CharField(max_length=8, null=True, blank=True)
    Reference = models.CharField(max_length=10, null=True, blank=True)
    WGS84Longitude = gps_field()
    WGS84Latitude = gps_field()
    CPElevation = models.CharField(max_length=9, null=True, blank=True)
    CPImage = models.ForeignKey(to=Image, related_name='image')
    CPImgType = models.CharField(max_length=15, null=True, blank=True)
    CPDescription = models.CharField(max_length=100, null=True, blank=True)
    CPMemo = models.CharField(max_length=50, null=True, blank=True)
