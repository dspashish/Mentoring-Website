from django.shortcuts import render, redirect, get_object_or_404
from users.models import CustomUser
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile
from mentor.models import HomeWork
from django.contrib import messages

def registerStudent(request):
    error = None
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST['last_name']
        username = request.POST['username']

        password1 = request.POST['password1']

        password2 = request.POST['password2']

        email = request.POST['email']
        std = request.POST.get("std")
        phone = request.POST.get("phone")
        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                error = "Username Taken"
                return render(request, template_name="register.html", context={"errors": error})
            elif CustomUser.objects.filter(email=email).exists():
                error = "Email Taken"
                return render(request, template_name="register.html", context={"errors": error})
            else:
                user = CustomUser.objects.create_user(username=username, password=password1,
                                                      email=email, first_name=first_name, last_name=last_name,
                                                      cat="student", std=std, phone_number=phone)
                user.save()
                u = auth.authenticate(username=username, password=password1)
                auth.login(request, u)
                user = get_object_or_404(CustomUser, username=request.user)

                a = Profile.objects.create(user=user)
                return redirect('/home/')
        else:
            error = "Password Do not match"
            return render(request, template_name="register.html", context={"errors": error})

    else:
        return render(request, template_name="register.html", context={"errors": error, "std": True})


def registerTeacher(request):
    error = None
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST['last_name']
        username = request.POST['username']

        password1 = request.POST['password1']

        password2 = request.POST['password2']

        email = request.POST['email']
        phone = request.POST["phone"]
        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                error = "Username Taken"
                return render(request, template_name="register.html", context={"errors": error})
            elif CustomUser.objects.filter(email=email).exists():
                error = "Email Taken"
                return render(request, template_name="register.html", context={"errors": error})
            else:
                user = CustomUser.objects.create_user(username=username, password=password1,
                                                      email=email, first_name=first_name, last_name=last_name,
                                                      cat="teacher", phone_number=phone, std="all")
                user.save()
                u = auth.authenticate(username=username, password=password1)
                auth.login(request, u)
                user = get_object_or_404(CustomUser, username=request.user)

                a = Profile.objects.create(user=user)
                return redirect('/home/')
        else:
            error = "Password Do not match"
            return render(request, template_name="register.html", context={"errors": error})

    else:
        return render(request, template_name="register.html", context={"errors": error})


def logout(request):
    auth.logout(request)
    return redirect("home")


def login(request):
    message = None

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:

            auth.login(request, user)

            return redirect("home")
        else:
            message = "Invalid Credentials"
            context = {"message": message}

            return render(request, template_name="login.html", context=context)

    else:
        return render(request, template_name="login.html")


@login_required
def profile(request):
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
