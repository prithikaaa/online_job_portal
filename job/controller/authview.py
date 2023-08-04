from django.shortcuts import render,redirect
from django.contrib import messages
from job.forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/visit/create")
    else:
     form=CustomUserForm()
    context = {'form':form}
    return render(request,"register.html", context)

def login(request):
   ''' if request.user.is_authenticated:
        messages.success(request, "You are already logged in")
        return redirect("/")

    if request.method == 'POST':
        name = request.POST.get('full_name')
        password = request.POST.get('password')
        user = authenticate(request, full_name=name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect("/")
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('/')'''
   return render(request, "login.html")
def logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")