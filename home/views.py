from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here. :(

def index(request):
   return render (request,"index.html")

def AboutUS(request):
   return render (request,"AboutUS.html")

def ContactUS(request):
   if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      subject = request.POST.get('subject')
      message = request.POST.get('message')
      ContactUS = Contact(name=name, email=email,subject=subject,message = message,date = datetime.today())
      ContactUS.save()
      messages.success(request,'Your message has been sent! Thank you.')
   return render(request,"ContactUS.html")

def JoinTeamForm(request):
   if request.method == "POST":
      name = request.POST.get('name')
      age = request.POST.get('age')
      gender = request.POST.get('gender')
      sport = request.POST.get('sport')
      position = request.POST.get('position')
      TeamName = request.POST.get('TeamName')
      JoinTeamForm = JTForm(name=name, age=age,gender=gender,sport=sport,position=position,TeamName=TeamName)
      JoinTeamForm.save()
      messages.info(request,'Congrats! Your have successfully joined the team.')
   return render (request,"JoinTeamForm.html")

def BookingForm(request):
   if request.method == "POST":
      date = request.POST.get('date')
      time_slot = request.POST.get('time_slot')
      BForm = BF(date=date, time_slot=time_slot)
      BForm.save()
      messages.info(request, 'Submitted. Please complete your payment for book!')

   return render (request,"BookingForm.html")


def Player(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)

        if user is not None:
            login(request,user)
            
            return redirect('PlayerProfile')
        
        else:
            messages.warning(request, 'Username or Password is incorrect')
            return redirect('Player')
      

        
    return render(request, "Player.html")

def LogoutPage(request):
   logout (request)
   return redirect('Player')

def Coach(request):  
   return render (request,"Coach.html")

def FieldAuthority(request):
   return render (request,"FieldAuthority.html")

def PlayerReg(request):
   if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1!= pass2:
            messages.warning(request, "Both passwords didn't match, please try again!")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save ()
            return redirect('Player')
   return render(request, "PlayerReg.html")

def CoachReg(request):
   return render (request,"CoachReg.html")

def FieldAuthorityReg(request):
   return render (request,"FieldAuthorityReg.html")

def TermsOfService(request):
   return render (request,"TermsOfService.html")



@login_required(login_url='Player')

def PlayerProfile(request):
   user = request.user
   context = {
               "uname": user.username,
               "email" : user.email,
            }
   return render (request,"PlayerProfile.html",context)

def Booked(request):
   return render (request,"Booked.html")


def JoinTeam1(request):
   return render (request,"JoinTeam1.html")

def JoinTeam2(request):
   if request.method == 'POST':
      print(request.POST['teams'])
   return render (request,"JoinTeam2.html")


def Field1(request):
   return render (request,"Field1.html")

def CoachProfile(request):
   return render (request,"CoachProfile.html")

def faProfile(request):
   return render (request,"faProfile.html")

def PaymentDone(request):
   return render (request,"PaymentDone.html")

def CT1(request):
   return render (request,"CT1.html")

def CT2(request):
   return render (request,"CT2.html")

def CT3(request):
   return render (request,"CT3.html")

def ChoosePayment(request):
   return render (request,"ChoosePayment.html")

def BanglaPayment(request):
   return render (request,"BanglaPayment.html")

def BideshiPayment(request):
   return render (request,"BideshiPayment.html")

def Matches(request):
   return render (request,"Matches.html")

def ChangePass(request):
   return render (request,"ChangePass.html")



















