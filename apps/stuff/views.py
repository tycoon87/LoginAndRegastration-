from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


def index (request):
    return render(request,'stuff/index.html',{"User": User.objects.all()})

def createUser (request):
    return render(request, 'stuff/register.html')

def show(request,User_id):
    return render(request, 'stuff/userPage.html', {"User": User.objects.get(id=User_id)})

def openEdit(request, User_id):
	return render(request, 'stuff/edit.html', {"User": User.objects.get(id=User_id)})

def Add(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/createUser')
    if request.POST['Password'] != request.POST['ConfirmPassword']:
        return render(request,'stuff/register.html')
    else:
        request.session['logOn'] = 'True'
        # request.session['Firstname'] = User.Firstname
        # request.session['Lastname'] = user.Lastname
        # request.session['Email'] = user.Email
        return render(request, 'stuff/userPage.html', {"User": User.objects.get(Email=request.POST['Email'])})

def edit(request,User_id):
        messages = User.objects.Edit_user(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
                return redirect('/openEdit/{{User.id}}')
        else:
            return render(request, '/show.html', {"User": User.objects.get(id=User_id)})

def delete(request,User_id):
	User.objects.get(id=User_id).delete()
	return redirect('/')

def Login(request):
    message = User.objects.LoginValidation(request.POST)

    if request.method == 'POST':
        attemptedValadate = User.objects.LoginValidation(request.POST)
        if message['status']:
            user = message['user']
            request.session['logOn'] = 'True'
            request.session['Firstname'] = user.Firstname
            request.session['Lastname'] = user.Lastname
            request.session['Email'] = user.Email
            request.session['userId'] = user.id

            return render(request, 'stuff/userPage.html', {"User": user})
        else:
            messages.error = "invalid username/password"
            return redirect('/')

def Logout(request):
    request.session.clear()
    return redirect('/')
