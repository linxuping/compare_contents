# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template,Context,RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
#from books.models import Publisher
#from base import *


@csrf_exempt
def test_compare(request):
  fp = open('autooperation/mergely.html')
  t = Template(fp.read())
  fp.close()
  html = t.render(Context({'lcont':'hello,world', 'rcont':'hello,worlD'}))
  return HttpResponse(html)
  