from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import *



def submit(request):
    data = request.POST
    data_ = dict(data)
    # data_.pop('csrfmiddlewaretoken')
    # print(data_)
    name = data_.get('names[]')
    address = data_.get('address[]')
    if name and address:
        count = 0
        for i in name:
            profile = Profile.objects.filter(name = name[count],address= address[count]).first()
            if profile: 
                return JsonResponse({"message":"Profile already exists",'error':True})
            else:
                profile = Profile(name = name[count],address= address[count])
                profile.save()
                count+=1
                return JsonResponse({"message":"Profiles added successfully",'error':False})

            
    return render(request,'core/index.html')