from django.shortcuts import render,redirect
from .models import Job,Company
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator

def job_list(request):
        search = request.GET.get('title')  

        if search:
            job = Job.objects.filter(title__icontains=search) 
        else:
            job = Job.objects.all()
        paginator = Paginator(job,5)
        page_number = request.GET.get('page')
        job = paginator.get_page(page_number)
                   
             
        return render(request,'job_list.html',{"job":job})


def job_detail(request,pk):
    job = Job.objects.get(id=pk)
    return render(request,'job_detail.html',{"job":job})


def job_create(request):
        if not request.user.is_authenticated:
              return redirect('login_user')
        company = Company.objects.all()
        print(company)
        if request.method == "GET":
            return render(request, "job_create.html",{"company":company})

        elif request.method == "POST":
            title = request.POST.get("title")
            company = request.POST.get("company")
            company = Company.objects.get(id=company)
            location = request.POST.get("location")
            description = request.POST.get("description")
            salary = request.POST.get("salary")
                    

            job = Job.objects.create(
            title=title,
            company=company,
            location=location,
            description=description,
            salary=salary
        )

        return redirect('job_list')



def job_delete(request,pk):
    if not request.user.is_authenticated:
         return redirect('login_user')
    job = Job.objects.get(id=pk)
    job.delete()
    return redirect('job_list')


def job_update(request,pk):
    if not request.user.is_authenticated:
         return redirect('login_user')
    job = Job.objects.get(id=pk)

    if request.method == "GET":
        return render(request,'job_update.html',{"job":job})



    elif request.method == "POST":
        title = request.POST.get("title")
        company = request.POST.get("company")
        company = Company.objects.get(id=company)
        location = request.POST.get("location")
        description = request.POST.get("description")
        salary = request.POST.get("salary")


        job.title = title
        job.company = company
        job.location = location
        job.description = description
        job.salary = salary

         
        job.save()

        return redirect('job_detail', pk=job.id)


def register_user(request):
     if request.method == "GET":
            return render(request,'register.html')

     elif request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirm_pass = request.POST.get("confirm_password")

            if password == confirm_pass:
                 user = User.objects.create_user(
                      username=username,
                      email=email,
                      password=password,
                  
                 )
                 return redirect('job_list')
     


def login_user(request):
     if request.method == "GET":
                return render(request,'login.html')

     elif request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")


            user = authenticate(
                 username=username,
                 password=password
            )

            if user:
                login(request,user)
                return redirect('job_list')


def logout_user(request):
     logout(request)
     return redirect('job_list')
    