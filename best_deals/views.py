from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm,BusinessForm
from .models import Profile,Business
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='/accounts/login/')
def index(request):
    try:
        current_user=request.user
        profile =Profile.objects.filter(username=current_user)
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
    except ObjectDoesNotExist:
        return render(request,'index.html')

    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def my_profile(request,id):
    current_user = request.user
    try:
        profile = Profile.objects.filter(username_id=id)
    except ObjectDoesNotExist:
        return render(request,'user_profile.html')

    return render(request,'user_profile.html',{"profiles":profile})




@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:

        form = ProfileForm()
    return render(request,'profile_form.html',{"form":form})

@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user=request.user
    
    businesses = Business.objects.all()

    return render(request,'business.html',{"businesses":businesses})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user=request.user
    

    if request.method=="POST":
        form =BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.owner = current_user
            business.save()

        return HttpResponseRedirect('/businesses')

    else:
        form = BusinessForm()

    return render(request,'business_form.html',{"form":form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('Index')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'update_profile.html',{"form":form})
