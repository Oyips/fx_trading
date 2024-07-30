from django.shortcuts import render
from django.http import HttpResponse
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')
from django.conf import settings
import ast

# Create your views here.
import random

balance=0.0
net_profit=0.0
profit=0.0



def home(request):
    with open(os.path.join(settings.BASE_DIR,'app1','net.txt'),'r') as f1:
        net_profit= ast.literal_eval(f1.read())
        
    with open(os.path.join(settings.BASE_DIR,'app1','count.txt'),'r') as f2:
        count=ast.literal_eval(f2.read())
    plt.plot(count,net_profit)
    plt.savefig(os.path.join(settings.BASE_DIR,'static','chart.png'))
    plt.close()
    return render(request,'home.html',{})

def trade(request,trading=False):
    global net_profit, profit, account
    return render(request,'trade.html')
    trading=request.GET("Trade")
    while trading=="True":
        profit=random.gauss()
        with open(os.path.join(settings.BASE_DIR,'app1','net.txt'),'r') as f1:
            net_profit= ast.literal_eval(f1.read()).append(profit)
        with open(os.path.join(settings.BASE_DIR,'app1','count.txt'),'r') as f2:
            count=ast.literal_eval(f2.read()).append().append(len(net_profit))
        with open(os.path.join(settings.BASE_DIR,'app1','net.txt'),'w') as f:
            net_profit= f.write(net_profit)
        with open(os.path.join(settings.BASE_DIR,'app1','count.txt'),'w') as f:
            f.write(count)
        return render(request,'trade.html')
        trade

        
        if balance==0:
            return  HttpResponse("Out of money")
        
            
    

    return render(request,'trade.html',{'balance':balance})

def login(request):
    pass
    
def account(request):
    return render(request,'account.html',{'net_profit':net_profit,'balance':balance,'profit':profit})

def index(request):
    pass
