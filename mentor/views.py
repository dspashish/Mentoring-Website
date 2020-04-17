from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import HomeWork, discuss, information
# Create your views here.
from users.models import CustomUser

def home(request):
    if request.user.is_authenticated:
        return redirect("/home/")
    return render(request, template_name="home.html")

def discussion(request):
    a = discuss.objects.all()
    context = {"obj": a}
    return render(request, template_name="discuss.html", context=context)

@login_required(login_url="/login/")
def main(request):
    if request.method == "POST":
        author = get_object_or_404(CustomUser, username=request.user)
        title = request.POST['title']
        name = request.user.first_name
        std = request.POST["std"]
        homework = request.POST["homework"]
        print(author, title, name, std, homework)
        a = HomeWork.objects.create(author=author,
                                    title=title,
                                    name=name,
                                    std=std,
                                    homework=homework)
        return redirect("/myhomework/")

    std = request.user.std
    obj = HomeWork.objects.filter(std=std)
    context = {"object": obj}

    return render(request, template_name="main.html", context=context)
    # obj = HomeWork.objects.all()
    # context = {"obj": obj}
    # return render(request, template_name="main.html")


def teachers(request):
    obj = CustomUser.objects.filter(cat="teacher")
    context = {"object_list": obj}
    return render(request, template_name="teachers.html", context=context)

def students(request):
    obj = CustomUser.objects.filter(cat="student")
    context = {"object_list": obj}
    return render(request, template_name="students.html", context=context)




def myHomeWork(request):
    user = get_object_or_404(CustomUser, username=request.user)
    obj = HomeWork.objects.filter(author=user)
    context = {
    "object_list": obj,
    }
    return render(request, template_name='myhomework.html', context=context)


def HomeWorkDetail(request, pk):
    obj = HomeWork.objects.get(pk=pk)
    context = {"object": obj}
    return render(request,template_name="detail.html",context=context)


def editDiscuss(request, pk):
    obj = discuss.objects.get(pk=pk)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        print("TITLE: ", title)
        print("CONTENT: ", content)
        obj.title = title
        obj.content = content
        obj.save()
        return redirect("/discuss/")
    return render(request, template_name="editDisscuss.html", context={"object": obj})


def disDetail(request, pk):
    obj = discuss.objects.get(pk=pk)
    context = {"object": obj}
    return render(request, template_name="disDetail.html", context=context)


def teachersDetail(request, pk):
    obj = CustomUser.objects.get(pk=pk)
    context = {"obj": obj}
    return render(request, template_name="td.html", context=context)




def create(request):
    if request.method == "POST":
        user = get_object_or_404(CustomUser, username=request.user)
        title = request.POST.get("title")
        content = request.POST.get("content")
        a = discuss.objects.create(author=user, title=title, content=content)
        return redirect('/discuss/')
    return render(request, template_name="creatediscuss.html")

def delete_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(discuss, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        if request.user.username == obj.author.username:
            obj.delete() 
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/discuss") 
  
    return render(request, "delete_view.html", context) 



def informations(request):
    obj = information.objects.all()
    context = {"obj": obj}
    return render(request, template_name="information.html", context=context)


def informationDetail(request, pk):
    obj = information.objects.get(pk=pk)
    context = {"object": obj}
    return render(request, template_name="id.html", context=context)