from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Auth,Complaint,Crime
from django.contrib.auth import authenticate,login,logout
import random

# Create your views here.
def homepage(request):
    return render(request,"crimemanagement/homepage.html")

def police(request):
    if request.method =="POST":
        user_name=request.POST["Username"]
        user_password=request.POST["password"]
        user= authenticate(request,username=user_name,password=user_password)
        if user:
            login(request,user)
            return render(request, "crimemanagement/police.html", {})
        else:
            html1="<html><body>Provide Valid Crendentials!!</body></html>" 
            return HttpResponse(html1)   
    else:
        pass            
        

def user(request):
    return render(request,"crimemanagement/user.html",{})

def complaint1(request):
    return render(request,"crimemanagement/complaint1.html",{})


def complaint_info(request):
    choices = list(range(1000))
    random.shuffle(choices)
    complaintnumber=choices.pop()
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    gender=request.POST.get('gender')
    date=request.POST.get('date')
    email=request.POST.get('email')
    phone_no=request.POST.get('p_no')
    address=request.POST.get('address')
    complaint=request.POST.get('subject')
    status="Submitted"
    comp_info=Complaint(complaintnumber=complaintnumber,fname=fname,lname=lname,gender=gender,date=date,mail=email,pno=phone_no ,add=address,desc=complaint,status=status)
    comp_info.save()

    return render(request,"crimemanagement/complaint_info.html",{'complaint_no':complaintnumber})  


def complaint_status(request):
    return render(request,"crimemanagement/complaint_status.html",{}) 

def view_status(request):
    comp_no=request.POST.get('comp_no')
    c_no = Complaint.complaint.filter(complaintnumber=comp_no).values('complaintnumber')
    fname = Complaint.complaint.filter(complaintnumber=comp_no).values('fname')
    lname = Complaint.complaint.filter(complaintnumber=comp_no).values('lname')
    gender = Complaint.complaint.filter(complaintnumber=comp_no).values('gender')
    date = Complaint.complaint.filter(complaintnumber=comp_no).values('date')
    mail = Complaint.complaint.filter(complaintnumber=comp_no).values('mail')
    pno = Complaint.complaint.filter(complaintnumber=comp_no).values('pno')
    add = Complaint.complaint.filter(complaintnumber=comp_no).values('add')
    desc = Complaint.complaint.filter(complaintnumber=comp_no).values('desc')
    status = Complaint.complaint.filter(complaintnumber=comp_no).values('status')
    #table1 = Complaint.crime.filter(complaintnumber=comp_no).values('complaintnumber','fname','lname','gender','date','mail','pno','add','desc','status')
   # table1= Complaint.crime.raw('SELECT * FROM crimemanagement_Complaint WHERE complaintnumber=%s' % comp_no)
    return render(request,"crimemanagement/view_status.html",{'c_no':c_no,'fname':fname,'lname':lname,'gender':gender,'date':date,'mail':mail,'pno':pno,'add':add,'desc':desc,'status':status})     
    
def contacts(request):
    return render(request,"crimemanagement/contacts.html")


def helplines(request):
    return render(request, "crimemanagement/helplines.html")


def enter(request):
    return render(request, "crimemanagement/entry.html")


def entry_details(request):
    crimenumber = request.POST.get('crimenumber')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    crime = request.POST.get('crime')
    age = request.POST.get('age')
    criminal_info = Crime(crimenumber=crimenumber,fname=fname,lname=lname,crime=crime, age=age)
    criminal_info.save()
    html3 = "<html><body>Criminal Details Recorded!!</body></html>"
    return HttpResponse(html3)

def records(request):
    return render(request,"crimemanagement/records.html")


def update(request):
    return render(request, "crimemanagement/update.html")
    

def update_status(request):
    comp_no = request.POST.get('comp_no')
    status = request.POST.get('status')
    Complaint.complaint.filter(complaintnumber=comp_no).update(status= status)
    html2 = "<html><body>Status Updated!!</body></html>"
    return HttpResponse(html2)

def view(request):
    return render(request,"crimemanagement/view.html",{})


def view_details(request):
    crimeno = request.POST.get('crimeno')
    cr_no = Crime.crimes.filter(crimenumber=crimeno).values('crimenumber')
    fname = Crime.crimes.filter(crimenumber=crimeno).values('fname')
    lname = Crime.crimes.filter(crimenumber=crimeno).values('lname')
    crime = Crime.crimes.filter(crimenumber=crimeno).values('crime')
    age = Crime.crimes.filter(crimenumber=crimeno).values('age')
   
    
    return render(request, "crimemanagement/view_details.html", {'cr_no': cr_no,'fname':fname,'lname':lname,'crime':crime,'age':age})



