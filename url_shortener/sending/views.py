from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UrlSerializer
from .models import Url
import random
from django.shortcuts import render, redirect
import string

@api_view(['GET'])
def get_site(request):
    if request.method=="GET":
      if request.GET.get('url'):
        url = request.GET.get('url')
        letters = string.ascii_lowercase 
        random_string = ''.join(random.choice(letters) for i in range(8))
        url_instance = Url.objects.create(url=url,random_string=random_string)
        return JsonResponse({'urls':url},safe=False)
      
      if request.GET.get('random_string'):
         random_str = request.GET.get('random_string')
         db_obj = Url.objects.get(random_string=random_str)
         redirect_url = db_obj.url
         return redirect(redirect_url)

@api_view(["POST"])
def add_site(request):
  if request.method == "POST":
    if request.POST.get('url'):
      url = request.POST.get('url')
      letters = string.ascii_lowercase 
      random_string = ''.join(random.choice(letters) for i in range(8))
      url_instance = Url.objects.create(url=url,random_string=random_string)
      return Response({'urls':url},safe=False)
         
         
         