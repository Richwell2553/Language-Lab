from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views import View

from .models import UserAccount

# Create your views here.
def home(request):
    context = {
    }
    return render(request,"landing_page.html",context=context)

@login_required(login_url="Authentication:login")
def dashboard(request):
    context = {
        "counts":range(20)
    }
    return render(request,"index.html",context=context)


@login_required(login_url="Authentication:login")
def tasks(request):
    context = {
        "counts":range(20)
    }
    return render(request,"tasks.html",context=context)

class ChatView(View):
    def get(self,request,username):
        friends = UserAccount.objects.all()
        friend_info = {
            "username":"graphene",
            "location":"Belarus/Russia",
            "profile_pic":"img/user.jpg",
            "is_active":True
        }

        user = UserAccount.objects.filter(username=username).first()
        if user:
            friend_info = user.__dict__

        context = {
            "friends":friends,
            "chat_info":friend_info
        }

        return render(request,"chats.html",context=context)
    
    def post(self,request):
        pass