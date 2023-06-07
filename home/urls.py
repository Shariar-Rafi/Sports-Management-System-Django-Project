from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path("",views.index,name = 'home'),
    path("home",views.index,name = 'home'),
    path("AboutUS",views.AboutUS,name = 'AboutUS'),
    path("ContactUS",views.ContactUS,name = 'ContactUS'),
    path("Player",views.Player,name = 'Player'),
    path("Coach",views.Coach,name = 'Coach'),
    path("FieldAuthority",views.FieldAuthority,name = 'FieldAuthority'),
    path("PlayerReg",views.PlayerReg,name = 'PlayerReg'),
    path("CoachReg",views.CoachReg,name = 'CoachReg'),
    path("FieldAuthorityReg",views.FieldAuthorityReg,name = 'FieldAuthorityReg'),
    path("TermsOfService",views.TermsOfService,name = 'TermsOfService'),
    path("PlayerProfile",views.PlayerProfile,name = 'PlayerProfile'),
    path("Booked",views.Booked,name = 'Booked'),
    path("JoinTeam1",views.JoinTeam1,name = 'JoinTeam1'),
    path("JoinTeam2",views.JoinTeam2,name = 'JoinTeam2'),
    path("JoinTeamForm",views.JoinTeamForm,name = 'JoinTeamForm'),
    path("Field1",views.Field1,name = 'Field1'),
    path("CoachProfile",views.CoachProfile,name = 'CoachProfile'),
    path("faProfile",views.faProfile,name = 'faProfile'),
    path("PaymentDone",views.PaymentDone,name = 'PaymentDone'),
    path("logout",views.LogoutPage,name = 'logout'),
    path("CT1",views.CT1,name = 'CT1'),
    path("CT2",views.CT2,name = 'CT2'),
    path("CT3",views.CT3,name = 'CT3'),
    path("BookingForm",views.BookingForm,name = 'BookingForm'),
    path("ChoosePayment",views.ChoosePayment,name = 'ChoosePayment'),
    path("BanglaPayment",views.BanglaPayment,name = 'BanglaPayment'),
    path("BideshiPayment",views.BideshiPayment,name = 'BideshiPayment'),
    path("Matches",views.Matches,name = 'Matches'),


    


    


path(
        'ChangePass/',
        auth_views.PasswordChangeView.as_view(
            template_name='regi/changePass.html',
            success_url = '/PlayerProfile'
        ),
        name='ChangePass'
    ),

]