from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model #better way to get user for long run

# better way to get user for long run
User = get_user_model()

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

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # this is how validation is done. in future, django form will take care of this. example only
        # username_exists = User.objects.filter(username__iexact=username).exists()
        # email_exists = User.objects.filter(username__iexact=email).exists()
        
        # below code is working. disable to prevent new registration
        # try:
        #     User.objects.create_user(username, email=email, password=password)
        # except:
        #     pass
    template_name = 'auth/register.html'
    return render(request, template_name, {})