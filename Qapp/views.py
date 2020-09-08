from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.template import Template,loader
from .models import accounts,question,answer
from .forms import signin_form,login_form,search_by_username,question_form,answer_form
from django import forms


#----------SERVER INDEX-------------------
def server_index(request):
	return redirect('/Qapp/')
	
	
#----------QAPP INDEX---------------------
def qapp_index(request):
	return render(request,'Qapp/Qapp_index.html')

 

#----------HOME--------------------
def home(request):
    try:
        a=accounts.objects.get(username=request.COOKIES['username'])
        qtemp=question.objects.all()
        if(len(qtemp)>=10):
            q=qtemp[-1:-10:-1]
        else:
            q=qtemp[::-1]
        #try:
        #    img_url=q.img1.url
        #except:
        #    img_url=""
        context= {
            'name':a.name,
            'username':a.username,
            'at_symbol':'@',
            'acc_color':a.acc_color,
            'feed':q
        #    'url':img_url
        }
        return render(request,"Qapp/home.html",context)
    except:
        return redirect("/Qapp/login/")


#----------SIGNIN--------------------
def signin(request):
    username_invalid_message="none"
    if request.method == "POST":
        form=signin_form(request.POST)
        if form.is_valid():
            try:
                a=accounts(name=form.cleaned_data['name'],username=form.cleaned_data['username'],password=form.cleaned_data['password'],acc_type="basic")
                a.save()
                response=redirect("/Qapp/home/")
                response.set_cookie("username",form.cleaned_data['username'])
                return response
            except:
                username_invalid_message="block"
    else:
        form=signin_form()
    context= {
        'form' :form,
        'inv_msg' :username_invalid_message
    }
    return render(request,"Qapp/signin.html",context)


#----------USER--------------------
def user(request,user_name):
    try:
        a=accounts.objects.get(username=user_name)
        context= {
            'uname':a.username,
            'name':a.name,
            'at_symbol':'@',
            'acc_color':a.acc_color
        }
    except:
        return redirect("Qapp/user/all_users")
    return render(request,"Qapp/user.html",context)


#----------ALL USERS--------------------
def all_users(request):
    a=accounts.objects.all()
    if request.method=="POST":
        form=search_by_username(request.POST)
        if form.is_valid():
            red_url="/Qapp/user/all_users/"+form.cleaned_data['username']+"/"
            return redirect(red_url)
    else:
        form=search_by_username()
    context= {
        'all_users':a,
        'form':form,
    }
    return render(request,"Qapp/allUsers.html",context)


#----------LOGIN--------------------
def login(request):
    invalid_message="none"
    if request.method == "POST":
        form=login_form(request.POST)
        if form.is_valid():
            try:
                a=accounts.objects.get(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                response=redirect("/Qapp/home/")
                response.set_cookie('username',str(a.username),max_age=3600*24)
                return response
            except:
                invalid_message="block"
    else:
        form=login_form()
    context= {
        'form' :form,
        'disp':invalid_message
    }
    return render(request,"Qapp/login.html",context)


#----------LOGOUT--------------------
def logout(request):
    if(request.COOKIES['username']):
        response=redirect("/Qapp/login/")
        response.delete_cookie('username')
        return response


#----------DELETE ACCOUNT--------------------
def delete_account(request):
    if(request.COOKIES['username']):
        response=redirect("/Qapp/signin/")
        accounts.objects.get(username=request.COOKIES['username']).delete()
        response.delete_cookie("username")
        return response


#----------GET PREMIUM----------------------
def get_premium(request):
    try:
        a=accounts.objects.get(username=request.COOKIES['username'])
        a.acc_type="requested"
        a.save()
        return redirect("/Qapp/home/")
    except:
        return redirect("/Qapp/login/")


#----------UPLOAD QUESTION------------------
def upload_question(request):
    if request.method=="POST":
        form=question_form(request.POST,request.FILES)
        if form.is_valid():
            try:
                try:
                    q=question.objects.get(Qtitle=form.cleaned_data['Qtitle'])
                    disp_coefficient="block"
                except:
                    form.save()
                    a=accounts.objects.get(username=request.COOKIES['username'])
                    q=question.objects.get(Qtitle=form.cleaned_data['Qtitle'])
                    q.asked_by=a
                    q.save()
                    return redirect("/Qapp/home/")
                #if null(q.img1)
            except:
                disp_coefficient="block"
            #a.asked_by=request.COOKIES['username']
            
    else:
        form=question_form()
        disp_coefficient="none"
    context={
        'form':form,
        'disp':disp_coefficient
    }
    return render(request,"Qapp/upload_q.html",context)


#---------------QUESTIONS BY USER--------------------
def questions_by_user(request,username):
    a=accounts.objects.get(username=username)
    q=question.objects.all().filter(asked_by=a)
    context={
        'account':a,
        'feed':q,
        'at_symbol':'@'
    }
    return render(request,'Qapp/userQ.html',context)


#--------------ALL QUESTIONS-------------------------
def all_questions(request):
    q=question.objects.all()
    context={
        'feed':q
    }
    return render(request,'Qapp/all_questions.html',context)


#------------SINGLE QUESTION VIEW--------------------
def question_view(request,qID):
    q=question.objects.get(id=qID)
    a=answer.objects.all().filter(ques=q)
    #HERE
    context={
        'ques':q,
        'ans':a
    }
    return render(request,"Qapp/ques_view.html",context)
    

#------------ADD ANSWER------------------------------
def add_answer(request,qID):
    q=question.objects.get(id=qID)
    if request.method=="POST":
        form=answer_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            ans=answer.objects.last()
            q=question.objects.get(id=qID)
            ans.ques=q
            ans.answered_by=accounts.objects.get(username=request.COOKIES['username'])
            ans.save()
            qUrl="/Qapp/question/"+qID+"/"
            return redirect(qUrl)
    else:
        form=answer_form()
    context={
        'form':form
    }
    return render(request,"Qapp/answer.html",context)




