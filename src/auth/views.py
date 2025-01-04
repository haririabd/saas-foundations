from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    template_name = 'auth/login.html'
    page_title = 'Login'
    context ={
        "page_title": page_title
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, template_name, context)

# def register_view(request):
#     template_name = 'auth/register.html'
#     return render(request, template_name, {})