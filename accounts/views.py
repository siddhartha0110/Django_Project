from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.


def register(request):
    if request.method == "POST":
        # Get Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            # Username Taken
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already Taken")
                return redirect('register')
            else:
                # Email Taken
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already in use")
                    return redirect('register')
                else:
                    # New User Register
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    # Login After Register(Immediately)
                    # auth.login(request,user)
                    #messages.success(request,"You are now logged in")
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'Registration Successfull')
                    return redirect('login')

        else:
            messages.error(request, "Passwords Do Not Match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "Logged Out")
        return redirect('index')
    return redirect('register')


def dashboard(request):
    user_contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
