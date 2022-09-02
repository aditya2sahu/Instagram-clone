from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import Usercreation
from django.contrib.auth import login,logout,authenticate
from .models import userprofile,profilepost,comment
from django.contrib.auth.models import User

# Create your views here.
def home(request):
   steam=profilepost.objects.filter(Q(profile_for_unlike_post__followers=request.user))
   return render( request,"Home.html",{"steam":steam})


def Login(request):
   userss=userprofile.objects.all()
   list=[]
   if request.method=="POST":
      users=request.POST['user']
      passs = request.POST['pass1']
      user= authenticate(username=users,password=passs)
      if user is not None:
         login(request, user)
         for i in userss:
            list.append(i.user)
         if request.user in list:
            return redirect('home')
         else:
            profile = userprofile(user=request.user)
            profile.save()
            return redirect('home')
   return render( request,"login.html")

def singup(request):
   form=Usercreation()
   if request.method=='POST':
      form=Usercreation(request.POST)
      if form.is_valid():
         form.save()
         return redirect('login')
   parameters={"forms":form}
   return render( request,"singup.html",parameters)

def profile(request):
   profile=userprofile.objects.get(user=request.user)
   getpost=profilepost.objects.filter(profile=request.user)
   postlen=len(getpost)
   getcomments=comment.objects.filter(profile=profile)
   commentlen=len(getcomments)
   return render( request,"profile.html",{"profile":profile,"post":getpost,"postcount":postlen,"commentlen":commentlen})

def Logout(request):
   logout(request)
   return  redirect('login')

def searchuserprofile(request,userid):
   profile=userprofile.objects.get(id=userid)
   getpost=profilepost.objects.filter(profile=profile.user)
   postlen=len(getpost)
   requests = userprofile.objects.get(user=request.user)
   return render( request,"searchuserprofile.html",{"pro":profile,"requests":requests,"post":getpost,"postcount":postlen})

def search(request):
   profile = userprofile.objects.all()
   if request.method=="GET":
      srch = request.GET.get('username',"")
      list=[]
      str="Please Enter Username"
      if srch == "":
         return render(request, "serach.html",{"warn":"plese Enter somthing"})
      else:
         profile = userprofile.objects.filter(user__username__icontains=srch)
         if len(profile)>0:
            dict = {"profile": profile,}
            return render(request, "serach.html", dict)
         else:
            return render(request ,"serach.html",{"warn":"not found "})

   return render( request,"serach.html")

def follow(request,id):
   profile=userprofile.objects.get(id=id)
   logeduser=userprofile.objects.get(user=request.user)
   if request.user in profile.followers.all():
      profile.followers.remove(request.user)
      logeduser.following.remove(profile.user)
      return redirect("searchuserprofile", userid=id)
   else:
      profile.followers.add(request.user)
      logeduser = userprofile.objects.get(user=request.user)
      logeduser.following.add(profile.user)
      return redirect("searchuserprofile",userid=id)


def post(request):
   if request.method == "POST":
      cap = request.POST.get("captions")
      file = request.FILES.get("myfiles")
      profile=userprofile.objects.get(user=request.user)
      saveimage = profilepost(profile=request.user, image=file, caption=cap, profile_for_unlike_post=profile)
      saveimage.save()
      return redirect('profile')
   return  render(request,"uploadpost.html")


def like(request,postid):
   getpost=profilepost.objects.get(id=postid)
   if  request.user in getpost.like.all():
      getpost.like.remove(request.user)
      return redirect('home')
   else:
      getpost.like.add(request.user)
      return redirect('home')


def comments(request,postid):
   getpost=profilepost.objects.get(id=postid)
   comments=comment.objects.filter(post__id=postid)
   list=comments
   return render(request,"comment.html",{"list":list,"getpost":getpost})

def upload(request,postid):
   if request.method=="POST":
      comments=request.POST.get('comment')
      pro=userprofile.objects.get(user=request.user)
      getpost = profilepost.objects.get(id=postid)
      commmnetsss=comment(user=request.user,profile=pro,post=getpost,comment=comments)
      commmnetsss.save()
      return redirect("home")



def likeview(request,postid):
   getpost=profilepost.objects.get(id=postid)
   users=userprofile.objects.all()
   list=[]
   for i in users:
      if i.user in getpost.like.all():
         list.append(i)
   print(list)      
   get=len(list)
   return  render(request,"likes.html",{"like":list,"range":range(0,get)})


def postfullview(request, postid):
   getpost=profilepost.objects.get(id=postid)
   getcomments=comment.objects.filter(post__id=postid)

   content={
      "post":getpost,
      "comments":getcomments
   }
   return render(request,"postfullview.html",content)



def delete(request,postid):
   profilepost.objects.filter(id=postid).delete()
   return redirect('profile')



























