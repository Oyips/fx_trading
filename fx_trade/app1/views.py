from django.shortcuts import render
from django.http import HttpResponse
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')
import time
from django.conf import settings
import ast


# Create your views here.
import random

stake=100.0
net_profit=0.0
profit=0.0
balance= 50
trading="False"



def home(request):
    with open(os.path.join(settings.BASE_DIR,'app1','net.txt'),'r') as f1:
        net_profit= ast.literal_eval(f1.read())
        
    with open(os.path.join(settings.BASE_DIR,'app1','count.txt'),'r') as f2:
        count=ast.literal_eval(f2.read())
    plt.plot(count,net_profit)
    plt.savefig(os.path.join(settings.BASE_DIR,'static','chart.png'))
    plt.close()
    return render(request,'home.html',{'balance':balance})

def trade(request):
    global net_profit, profit, balance,trading
    
    if request.method=="POST":
        trading=request.POST["Trade"]
        
        print(trading)
        if trading=="False":
            return render(request,'trade.html',{'balance':balance,'profit':profit})
        while trading=="True":
            time.sleep(10)
            profit=random.gauss(0,1)
            with open(os.path.join(settings.BASE_DIR,'app1','net.txt'),'r') as f1:
                profits= ast.literal_eval(f1.read())
                profits.append(profit)
                #print(profits)
            with open(os.path.join(settings.BASE_DIR,'app1','count.txt'),'r') as f2:
                count=ast.literal_eval(f2.read())
                count.append(len(profits))
            print(count)
            with open(os.path.join(settings.BASE_DIR,'app1','net.txt'),'w') as f:
                f.write(str(profits))
            with open(os.path.join(settings.BASE_DIR,'app1','count.txt'),'w') as f:
                f.write(str(count))
            profits = [int(num) for num in profits]
            count = [int(num) for num in count]
            net_profit=sum(profits)
            balance=stake+net_profit
    
            if balance<=0:
                trading="False"
                return  HttpResponse(request,"Out of money")
    
           
            
            
         
        
        return render(request,'trade.html',{'balance':balance,'profit':profit})
        
        
    else :
        
       
        while trading=="True":
            time.sleep(10)
            profit=random.gauss(0,1)
            with open(os.path.join(settings.BASE_DIR,'app1','net.txt'),'r') as f1:
                profits= ast.literal_eval(f1.read())
                profits.append(profit)
                #print(profits)
            with open(os.path.join(settings.BASE_DIR,'app1','count.txt'),'r') as f2:
                count=ast.literal_eval(f2.read())
                count.append(len(profits))
            print(count)
            with open(os.path.join(settings.BASE_DIR,'app1','net.txt'),'w') as f:
                f.write(str(profits))
            with open(os.path.join(settings.BASE_DIR,'app1','count.txt'),'w') as f:
                f.write(str(count))
            profits = [int(num) for num in profits]
            count = [int(num) for num in count]
            net_profit=sum(profits)
            balance=stake+net_profit

            if balance<=0:
                trading="False"
                return  HttpResponse(request,"Out of money")
            

        return render(request,'trade.html',{'balance':balance,'profit':profit})    
        
            
    

    

def login(request):
    pass
    
def account(request):
    return render(request,'account.html',{'net_profit':net_profit,'balance':balance,'profit':profit})

def index(request):
    pass
