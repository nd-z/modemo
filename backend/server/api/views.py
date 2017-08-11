# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.
class FBView(APIView):
	# initialize the bias analyzer here

	#/api/login
	def post(self, request):
		# get values from request and call the main handler for the heavy lifting


class AnalyzeView(APIView):
	# initialize the bias analyzer here

	#/api/analyze
	def post(self, request):
		# get the url from request and call main handler for heavy lifting