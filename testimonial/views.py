from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from testimonial.forms import LoginForm,TestimonialForm
from testimonial.models import Testimonial
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['email']
        password =  request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            print("else")
    form=LoginForm()
    context = {'form': form,}
    return render(request,'login.html',context) 

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def testimonial_view(request):  
    print(request)  
    testimonial_list=Testimonial.objects.all()
    page = request.GET.get('page', 1)  
    paginator = Paginator(testimonial_list, 2)
    try:
        testimonials = paginator.page(page)
    except PageNotAnInteger:
        testimonials = paginator.page(1)
    except EmptyPage:
        testimonials = paginator.page(paginator.num_pages)

      
    context={'testimonials':testimonials}   
    return render(request, 'testimonial-view.html',context)   

@login_required
def add_new(request):
    print(request)
    if request.method == 'POST':
        form = TestimonialForm(request.POST,files=request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("view")        
    else:
        form = TestimonialForm()
    context = {'form': form}
    return render(request,'testimonial-create.html',context) 

@login_required
def testimonial_update(request,pk):
    testimonial=Testimonial.objects.get(id=pk)
    if request.method == 'POST':
        form = TestimonialForm(request.POST,files=request.FILES,instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect("view",)
    else:
        form = TestimonialForm(instance=testimonial)
    context = {'form': form,'testimonial': testimonial}
    return render(request,'testimonial-create.html',context) 

@login_required
def testimonial_delete(request, pk):
    if request.method == 'POST':
        testimonial= Testimonial.objects.get(pk=pk)
        testimonial.delete()
        return redirect('view') 


def logout_user(request):
    logout(request)
    return redirect('/')

def search(request):        
    if request.method == 'GET':   
        testimonial_name =  request.GET['search']        
        try:
            status = Testimonial.objects.filter(title__icontains=testimonial_name) 
            # print(status)
        except Testimonial.DoesNotExist:
            status = None    
        return render(request,"testimonial-view.html",{"testimonial":status})
    else:
        return render(request,"testimonial-view.html",{})    

        

