from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,User
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login,logout
from .models import Msg
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('all_user')
    form=AuthenticationForm()
    return render(request,'login.html', {'form':form})

def chat(request,id):
    user=request.user
    receiver=User.objects.get(id=id)
    chat_sender=Msg.objects.filter(sender=user,receiver=receiver)
    chat_receive=Msg.objects.filter(sender=receiver,receiver=user)
    data={
    'receiver':User.objects.get(id=id),
    'sender':request.user
    }
    return render(request,'chat.html',{'data':data,'chat_sender':chat_sender,'chat_receive':chat_receive})


def  logout_view(request):
    logout(request)
    return redirect('login')

def all_user(request):
    user=User.objects.all()
    return render(request,'user.html',{'user_list':user})

def com(request):
    sender = request.user
    receiver=User.objects.get(username=request.POST.get('receiver'))
    chat=request.POST.get('msg')
    Msg.objects.create(receiver=receiver,sender=sender,chat=chat)

    return JsonResponse('hit',safe=False)


def receive_data(request):
    user=request.user
    receiver = User.objects.get(username=request.POST.get('receiver'))
    a= Msg.objects.filter(receiver=user, sender=receiver).last()
    data={'id':a.id,'chat':a.chat}
    return JsonResponse(data)



def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('all_user')
    form=UserCreationForm()
    return render(request,'register.html',{'form':form})