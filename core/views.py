from django.shortcuts import render

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
            profile = Profile(name = name[count],address= address[count])
            profile.save()
            count+=1
    print("done")
            
    return render(request,'core/index.html')