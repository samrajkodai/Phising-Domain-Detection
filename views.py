from django.shortcuts import render,redirect
from . import ml_predict

def home(request):
    return render(request,"index.html")

def home2(request):
    return render(request,'home2.html')

def result(request):

    url=request.GET['url']

    qty_slash_url=0
    qty_equal_url=0
    length_url=len(url)
    qty_hyphen_params=0
    qty_percent_params=0
    qty_dot_domain=0

    for i in url:
        if i=='/':
            qty_slash_url+=1
        elif i=="=":
            qty_equal_url+=1
        elif i=="-":
            qty_hyphen_params+=1
        elif i=="%":
            qty_percent_params+=1
        elif i==".":
            qty_dot_domain+=1
  
    directory_length=int(request.GET["directory_length"])
    asn=int(request.GET['asn'])
    time_domain_activation=int(request.GET['time_domain_activation'])
    ttl_hostname=int(request.GET['ttl_hostname'])

    predict=ml_predict.prediction_model(qty_slash_url,qty_equal_url,length_url,qty_dot_domain,directory_length,qty_hyphen_params,qty_percent_params,asn,time_domain_activation,ttl_hostname)
    return render(request,"result.html",{"prediction":predict})