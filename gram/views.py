from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from gram.forms import CommentsForm, PictureForm, ProfileForm
from gram.models import Comments, Picture, Profile
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    post = Picture.objects.all()
    profile = Profile.objects.filter()
   

    return render(request,'all-grams/home.html',{'post':post,'profile':profile})

def explore(request):
    post = Picture.objects.all()
    return render(request,'all-grams/explore.html',{'post':post})

def profile(request):
    profile = Profile.objects.get(user=request.user)
    post = Picture.objects.filter(user=request.user)
    
    return render(request,'all-grams/profile.html',{'profile':profile,'post':post})

def single_profile(request,pk):
      profile = Profile.objects.get(pk=pk)

      return render(request,'all-grams/profile.html',{'profile':profile})

def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
          

            return redirect('profile')
        else:
            return redirect('update_profile')

    else: 
       form = ProfileForm(instance=request.user.profile)
       return render (request,'all-grams/update_profile.html',{"form":form})

def make_a_post(request):
    
    post = Picture(user=request.user)

    if request.method == 'POST':
        
         form = PictureForm(request.POST,request.FILES,instance=post)
         if form.is_valid():
            form.save()
            
            return redirect('home')
         else:
           
            return redirect('Make_a_post')


    else:
        form = PictureForm(instance=post)
        return render(request,'all-grams/post.html',{"form":form})

def single_post(request,pk):
      post = Picture.objects.get(pk=pk)

      return render(request,'all-grams/photo.html',{'post':post})

def comment(request,pk):
    """This will handle the commenting on a particular post
    Args:
        request ([type]): [description]
        pk ([type]): [description]
    """
    if request.method == 'POST':
        post = get_object_or_404(Picture,pk=pk)
        comment = Comments(user = request.user,image = post, form = CommentsForm(request.POST),comment = request.POST['comment'])
        comment.save()
        return HttpResponseRedirect(reverse('home'))

def like(request,pk):
    """This will handle adding a like to a post
    Args:
        request ([type]): [description]
        pk ([type]): [description]
    """
    post = get_object_or_404(Picture,pk=pk)
    post.like_image(request.user)
    return HttpResponseRedirect(reverse('home'))

def FollowView(request,pk):
   
    profile = get_object_or_404(Profile,pk=pk)
    profile.follows.add(request.user)
   
    return HttpResponseRedirect(reverse('profile'))

 