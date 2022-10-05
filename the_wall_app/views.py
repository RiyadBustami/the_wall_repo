from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from login_registration_app.models import User
from the_wall_app.models import Message,Comment
from the_wall_app import models

# Create your views here.

def index(request):
    if 'id' in request.session:
        context={
            'logged_user':User.objects.get(id=request.session['id']),
            'messages':Message.objects.all().order_by('-created_at'),
            
        }
        print(context['messages'])

        return render(request,"wall.html",context)
    else:
        return redirect('/')

def add_message(request):
    if request.method == 'POST':
        models.create_message(request)
        return redirect('/wall/')

def add_comment(request):
    if request.method == 'POST':
        message= Message.objects.get(id=request.POST['message_id'])
        user= User.objects.get(id=request.session['id'])
        comment= request.POST['comment']
        Comment.objects.create(message=message,user=user,comment=comment)
    return redirect('/')

def delete_message(request):
    if request.method == 'POST':
        deleted_message=Message.objects.get(id=request.POST['delete_message_id'])
        print(deleted_message)
        deleted_message.delete()
    return redirect('/')

def delete_comment(request):
    if request.method == 'POST':
        deleted_comment=Comment.objects.get(id=request.POST['delete_comment_id'])
        print(deleted_comment)
        deleted_comment.delete()
    return redirect('/')