from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def allcategories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'category.html',context)
def allproducts(request,p):               #here p receives the category id
    c=Category.objects.get(id=p)           #reads a particular category object using id
    p=Product.objects.filter(category=c)    # reads all products under a particular category object
    context={'cat':c,'product':p}

    return render(request,'product.html',context)

def productdetails(request,p):
    pro=Product.objects.get(id=p)
    context={'product':pro}
    return render(request,'detail.html',context)
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        e=request.POST.get('e')
        fn=request.POST['f']
        ln=request.POST['l']
        if(cp==p):
            user=User.objects.create_user(username=u,password=p,email=e,first_name=fn,last_name=ln)
            user.save()
            return redirect('shop:categories')

    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        print(u,p)
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:categories')

        else:
            messages.error(request,"invalid credentials")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('shop:categories')

def addcategory(request):
    if(request.method=="POST"):
        n=request.POST['n']
        i= request.FILES['i']
        d = request.POST['d']

        c=Category.objects.create(name=n,image=i,desc=d)
        c.save()
        return redirect('shop:categories')
    return render(request,'addcategory.html')

def addproduct(request):
    if (request.method == "POST"):
        n = request.POST['n']
        i = request.FILES['i']
        d = request.POST['d']
        s=request.POST['s']
        p=request.POST['p']
        c=request.POST['c']   #reads the category name from form field
        cat=Category.objects.get(name=c)  #category object/record matching with category name c

        p=Product.objects.create(name=n,image=i,desc=d,stock=s,price=p,category=cat) #assigns each value to product fields
        p.save()
        return redirect('shop:categories')


    return render(request, 'addproduct.html')

def addstock(request,p):
    product=Product.objects.get(id=p)

    if(request.method=="POST"): #after form submission
        product.stock=request.POST['n']
        product.save()
        return redirect('shop:categories')


    context={'pro':product}
    return render(request,'addstock.html',context)
