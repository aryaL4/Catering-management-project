from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .models import* 
from django.contrib.auth.models import User




def firstpage(request):
    return render(request,'first_page.html')



def cater_reg(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 =request.POST.get('password')
        pass2 =request.POST.get('confirm_password')
        if pass1== pass2:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request,'username already exists')
                return render(request,'caters/register.html')
            else:
                regt = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    password=pass1,
                    is_cater=True,
                    
                )
                messages.success(request,'Registraion successful, please login')
                regt.save()
                return redirect('cater_log')
        else:
            messages.error(request,'password not matching')
   
    return render(request, 'caters/register.html')

def cater_log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomUser.objects.filter(username=username).first()

      
        if user is not None and user.check_password(password) and user.is_cater:
            login(request, user)
            return redirect('cater_home')
        else:
            messages.error(request, 'Invalid login attempt')
    return render(request, 'caters/login.html')


def cater_home(request):
    return render(request,'caters/home.html')
 

# #######category#########

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES.get('img')
        cate = Catagory.objects.create(name=name, img=img)
        return redirect('add_category')

    return render(request, 'caters/add_cata.html')

def view_category(request):
    categories = Catagory.objects.all()
    return render(request, 'caters/view_cata.html', {'categories': categories})

def delete_category(request, id):
    category = Catagory.objects.get(id=id)
    category.delete()
    return redirect('view_category')

# ##########prod


def add_product(request):
    categories = Catagory.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES.get('image')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        quant = request.POST.get('quantity')
        category_id = request.POST.get('category')  
        product = Product.objects.create(
            name=name,
            image=img,
            desc=desc,
            price=price,
            quantity=quant,
            user=request.user,
            category_id=category_id  # Corrected to use the correct category ID
        )
        return redirect('add_product')

 
    return render(request, 'caters/add_product.html', {'categories': categories})

def view_produc(request):
    produ = Product.objects.all()
    return render(request,'caters/view_product.html',{'produ':produ})


def update_product(request, product_id):
    selected_product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        selected_product.category = Catagory.objects.get(id=request.POST.get('category'))
        selected_product.name = request.POST.get('name')
        selected_product.desc = request.POST.get('desc')
        selected_product.price = request.POST.get('price')
        selected_product.quantity = request.POST.get('quantity')

        if 'image' in request.FILES:
            selected_product.image = request.FILES['image']

       
        selected_product.save()
        return redirect('view_product')


    categories = Catagory.objects.all()
    return render(request, 'caters/updateproduct.html', {'selected_product': selected_product, 'categories': categories})




def delete_product(request, id):
    prod = Product.objects.get(id=id)
    prod.delete()
    return redirect('view_produc')


def requestform(request):
    buynow_list = Buynow.objects.all()
    
    if request.method == 'POST':
        buy_form = Buynow()
        buy_form.username = request.POST.get('name')
        buy_form.category = request.POST.get('category')
        buy_form.quantity = request.POST.get('quantity')
        buy_form.price = request.POST.get('price')
        buy_form.address = request.POST.get('address')
        
        buy_form.save()

    context = {'buynow_list': buynow_list}
    return render(request, 'caters/requestview.html', context)

from django.http import Http404

def finished(request, pk):
    try:
        finish = Buynow.objects.get(id=pk)
        finish.finished = True
        finish.save()
        return redirect('requestform')
    except Buynow.DoesNotExist:
       
        raise Http404("Buynow object not found")



def delete(request,pk):
    dele =Buynow.objects.get(id=pk)
    dele.delete()
    return redirect('requestform')


def update_profile(request,pk):
    upd = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        new_email = request.POST.get('email')
        if new_email:
            upd.email = new_email
            upd.save()
            return redirect('cater_home')
    return render(request,'caters/update_profile.html',{'upd':upd})    





# #########user###########

def user_registration(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 =request.POST.get('password')
        pass2 =request.POST.get('confirm_password')
        if pass1== pass2:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request,'username already exists')
                return render(request,'user/registration.html')
            else:
                regt = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    password=pass1,
                    is_user=True,
                    
                )
                messages.success(request,'Registraion successful, please login')
                regt.save()
                return redirect('user_log')
        else:
            messages.error(request,'password not matching')
   
    return render(request, 'user/registration.html')


def user_log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomUser.objects.filter(username=username).first()

      
        if user is not None and user.check_password(password) and user.is_user:
            login(request, user)
            return redirect('user_home')
        else:
            messages.error(request, 'Invalid login attempt')
    return render(request, 'user/login.html')


def user_home(request):
     categories = Catagory.objects.all()
     featured_products = Product.objects.all()
    
     context = {
        'categories':categories,
        'featured_products':featured_products,
        
    }
   
     return render(request,'user/index.html',context)


def log_out(request):
    logout(request)
    return redirect("firstpage")


def updateuser_profile(request,pk):
    upd = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        new_email = request.POST.get('email')
        if new_email:
            upd.email = new_email
            upd.save()
            return redirect('updateuser_profile')
    return render(request,'user/update_profile.html',{'upd':upd}) 

def view_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'user/product_view.html', {'product': product})





def buy_now(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        name=str(request.POST.get('name'))
        quantity = int(request.POST.get('quantity'))
        category_id = int(request.POST.get('category'))
        total_price = quantity * product.price
        address = request.POST.get('address')
        
        selected_category = Catagory.objects.get(id=category_id)

        buynow = Buynow(product=product,username=name, quantity=quantity, price=total_price, address=address, category=selected_category)
        buynow.save()
        
        return redirect('view_req')

    context = {'product': product, 'categories': Catagory.objects.all()}
    return render(request, 'user/buy_nowform.html', context)






# user req form#########

def view_req(request):
    buynow_list = Buynow.objects.all()
    
    if request.method == 'POST':
        buy_form = Buynow()
        buy_form.username = request.POST.get('name')
        buy_form.category = request.POST.get('category')
        buy_form.quantity = request.POST.get('quantity')
        buy_form.price = request.POST.get('price')
        buy_form.address = request.POST.get('address')
        
        buy_form.save()

    context = {'buynow_list': buynow_list}
    return render(request, 'user/view_req.html', context)





