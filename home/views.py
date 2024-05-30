from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from datetime import datetime
from home.models import Contact
from home.models import Notes
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
# Create your views here.

def index(request):
    # return HttpResponse("home s hoo")
    arr = Notes.objects.all().order_by('-date')
    context = {
        "all_notes" : arr,
        "home_active" : "active"
    }
    return render(request,"index.html",context)

def addNote(request):
    if request.user.is_anonymous:
        return redirect("/login")


    if request.method == "POST":
        email = request.POST.get("email")
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        time = datetime.today()
        notes = Notes(email = email, title = title, desc = desc, date = time)
        notes.save()
        return JsonResponse({'message': 'success'})

    context = {
        "notes_active" : "active"
    }
    return render(request,"addNotes.html",context)

def about(request):
    context = {
        "about_active" : "active"
    }
    return render(request,"about.html",context)

def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        text = request.POST.get("text")
        time = datetime.today()
        contact = Contact(email = email, text = text, date = time)
        contact.save()
        messages.success(request, "Query sent Successfully.",extra_tags="contact")
    
    context = {
        "contact_active" : "active"
    }
    return render(request,"contact.html",context)

def signup(request):
    if not request.user.is_anonymous:
        return redirect("/")
    
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        first = request.POST.get("first")
        last = request.POST.get("last")
        password = request.POST.get("password")
        try:
            user = User.objects.create_user(email = email, username=username, first_name= first, last_name=last, password=password)
            user.save()
            messages.success(request, "Account Created Successfully.",extra_tags="signup")
            return redirect("/login")
        except:
            messages.error(request, "Username or email already exists.", extra_tags="signup")
    
    if request.method == 'GET' and request.GET.get('isUsername') == 'True':
        # print("ll")
        username = request.GET.get("username") 
        found = User.objects.filter(username = username)
        if len(found) > 0:
            return JsonResponse({"messages":"fail"})
        else:
            return JsonResponse({"messages":"success"})
        
    if request.method == 'GET' and request.GET.get('isEmail') == 'True':
        # print("ll")
        email = request.GET.get("email") 
        found = User.objects.filter(email = email)
        if len(found) > 0:
            return JsonResponse({"messages":"fail"})
        else:
            return JsonResponse({"messages":"success"})
            
        

    context = {
        "signup_active" : "active"
    }
    
    return render(request,"signup.html",context)



def loginUser(request):
    if not request.user.is_anonymous:
        return redirect("/")

    context = {
        "login_active" : "active"
    }

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            print("not logged in")

    return render(request,"login.html",context)

def logoutUser(request):
    if request.user.is_anonymous:
        return redirect("/")
    
    logout(request)
    return redirect("/login")


