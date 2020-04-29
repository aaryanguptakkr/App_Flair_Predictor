from django.shortcuts import render
from .forms import uploadForm
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Upload, Ans
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .rscraper import flair_predictor
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import os, shutil, time
from django.contrib.auth.decorators import login_required
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UploadSerializer
from rest_framework import generics
from rest_framework.views import APIView


def uploadView(request):
    
    if request.method == "POST":
        form = uploadForm(request.POST, request.FILES)
        if(form.is_valid()):
            file=request.FILES['files']
            data=file.read()
            y=""
            for x in data:
                y+=chr(x)
            ans={}
            for line in y.split("\n"):
                if(line!=""):
                    # print(flair_predictor(line)[0])
                    ans[line]=flair_predictor(line)[0]
            # json_str = serializers.serialize('json', ans)
            # response = HttpResponse(json_str, content_type='application/json')
            # response['Content-Disposition'] = 'attachment; filename=export.json'
            return JsonResponse(ans, safe=False)
                
    else:
        form = uploadForm()
    return render(request, "index.html", {'form':form})
    

class FileUploadView(APIView):
    serializer_class = UploadSerializer

    def post(self, request, format='txt'):
        up_file = request.FILES['upload_file']
        destination = open(up_file.name, 'wb+')
        data=up_file.read()
        y=""
        for x in data:
            y+=chr(x)
        ans={}
        for line in y.split("\n"):
            if(line!=""):
                # print(flair_predictor(line)[0])
                ans[line]=flair_predictor(line)[0]

        # ...
        # do some stuff with uploaded file
        # ...
        return Response(ans, status.HTTP_201_CREATED)