from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms  import AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages

from .forms import RegistroForm



class Register(View):

    def get(self, request):
        form= RegistroForm()
        return render(request,"register/register.html", {"form":form})

    def post(self, request):
        form= RegistroForm(request.POST)

        if form.is_valid():

         usuario=form.save()        
         login(request, usuario)
         return redirect('Home')
        
        

        return render(request, "register/register.html", {"form": form})
           
def log_out(request):
     logout(request)
     return redirect('Home') 

 
def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username") 
            contra = form.cleaned_data.get("password")
            usuario = authenticate(request, username=username, password=contra) 
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")

    form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})
    
    