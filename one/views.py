from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
import sweetify
from one.models import *
from one.forms import *

# Create your views here.


def home(request):
    if request.method=="POST":
        name=request.POST.get('contactName')
        email=request.POST.get('contactEmail')
        subject=request.POST.get('contactSubject')
        message=request.POST.get('contactMessage')
        z=Feedback.objects.get_or_create(name=name,email=email,subject=subject,message=message)
    return render(request,'webpage.html')


def userlogin(request):
    if request.method=="POST": 
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect(allphotos)
        else:
            print("User not found")
    return render(request,'signin.html',{})


def registeruser(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password1')
        user=authenticate(request,username=username,password=password)
        if form.is_valid():
            form.save()
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect(createprofile)       
    form=UserForm()
    context={
        'form':form,
    }
    return render(request,'signup.html',context)

@login_required(login_url='signin')
def createprofile(request):
    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            formobj=form.save(commit=False)
            formobj.user=request.user
            formobj.save()
            return redirect(allphotos)  
    form=ProfileForm()
    context={
        'form':form,
    }
    return render(request,"create-profile.html",context)


@login_required(login_url='signin')
def userlogout(request):
    if request.method=="POST":
        logout(request)
        return redirect(home)
    return render(request,'signout.html',{})


@login_required(login_url='signin')
def openprofile(request):
    check=Profile.objects.filter(user=request.user)
    if not check:
        return redirect(createprofile)
    profile=Profile.objects.get(user=request.user)
    image=Image.objects.filter(user=request.user).count()
    album=Albumn.objects.filter(user=request.user).count()
    context={
        'profile':profile,
        'images':image,
        'albums':album,
    }
    return render(request,"profile.html",context)



@login_required(login_url='signin')
def imageupload(request):
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.cleaned_data.get('image')
            albumn=request.POST.get('albumn')
            albumn=albumn.replace(" ","")
            albumn=albumn.capitalize()
            alb=Albumn.objects.get_or_create(user=request.user,albumn=albumn)
            albid=Albumn.objects.get(user=request.user,albumn=albumn)
            Image.objects.get_or_create(albumn_id=albid.id,user=request.user,image=image)
            return redirect(allphotos)
              
    form=ImageForm()
    context={
        'form':form,
    }
    return render(request,"upload.html",context)

@login_required(login_url='signin')
def editprofile(request):
    r=Profile.objects.get(user=request.user)
    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES,instance=r)
        if form.is_valid():
            formobj=form.save(commit=False)
            formobj.user=request.user
            formobj.save()
            return redirect(openprofile)  
    form=ProfileForm(instance=r)
    context={
        'form':form,
    }
    return render(request,"edit-profile.html",context)

@login_required(login_url='signin')
def allphotos(request):
    q=Image.objects.filter(user=request.user)
    context={
        'pics':q
    }
    return render(request,'all-photos.html',context)


@login_required(login_url='signin')
def albumns(request):
    a=Albumn.objects.filter(user=request.user)
    context={
        'albumns':a
    }
    return render(request,'albumn.html',context)


@login_required(login_url='signin')
def openalbumn(request,id):
    a=Image.objects.filter(albumn=id)
    albumn=Albumn.objects.get(id=id)
    context={
        'pics':a,
        'albumn':albumn,
    }
    return render(request,'openalbumn.html',context)


@login_required(login_url='signin')
def favourites(request):
    fav=Favourites.objects.filter(user=request.user)
    context={
        'favs':fav,
    }
    return render(request,'favourites.html',context)


@login_required(login_url='signin')
def openimage(request,id):
    pic=Image.objects.get(id=id)
    fav=Favourites.objects.filter(image=pic)
    context={
        'pic':pic,
        'favourite':fav,
    }
    return render(request,'openimage.html',context)


@login_required(login_url='signin')
def addtofavourites(request,id):
    pic=Image.objects.get(id=id)
    Favourites.objects.get_or_create(user=request.user,image=pic)
    return redirect(favourites)


@login_required(login_url='signin')
def removefromfavourites(request,id):
    f=Image.objects.get(id=id)
    h=f.favourites_set.all()
    h.delete()
    return redirect(favourites)
   

@login_required(login_url='signin')
def deleteimage(request,id):
    f=Image.objects.get(id=id)
    f.delete()
    return redirect(allphotos)


