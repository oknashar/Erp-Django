from django.shortcuts import get_object_or_404, redirect, render
from .forms import CategoryForm,ColorForm,TypeForm,creatorForm
from .models import Category,Color,Type,creator
from .filters import ColorFilter,CategoryFilter,TypeFilter,creatorFilter
from product.models import Order, OrderItem, Product
from product.filters import Order2Filter, OrderFilter, ProductFilter
from product.forms import ProductForm
from django.contrib import messages
from django.views.generic import  DeleteView,View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from employe.models import Absense,Employe
import datetime

# Create your views here.

def color_list(request):
    ListColor = Color.objects.all()

     ##filters##
    my_filter = ColorFilter(request.GET ,queryset=ListColor)
    colorList = my_filter.qs

   

    context = {
        'colors':colorList,
        'my_filter':my_filter
    }
    return render(request,'Color/colors.html',context)

def addColor(request):
    if request.method=='POST':
        form = ColorForm(request.POST)

        if form.is_valid:
            myform = form.save(commit=False)
            myform.save()
            return redirect('/color')
    else:
        form =ColorForm()
    context={'form':form}
    return render(request,'Color/add_color.html',context)

def edit_Color(request,id):
    post = get_object_or_404(Color ,id=id )
    if request.method=='POST':
        form=ColorForm(request.POST,instance=post)
        if form.is_valid():
            newform=form.save(commit=False)
            newform.user=request.user
            newform.save()
            return redirect('/color')

    else:
        form = ColorForm(instance=post)
    
    context = {
        'form': form ,
    }

    return render(request,'Color/editcolor.html',context)

def delete_Color(request,id):
    color =Color.objects.get(id=id).delete()

    return redirect('/color')

def Category_list(request):
    ListCategory = Category.objects.all()

     ##filters##
    my_filter = CategoryFilter(request.GET ,queryset=ListCategory)
    categoryList = my_filter.qs

   

    context = {
        'categorys':categoryList,
        'my_filter':my_filter
    }
    return render(request,'Category/categorys.html',context)

def addCategory(request):
    if request.method=='POST':
        form = CategoryForm(request.POST)

        if form.is_valid:
            myform = form.save(commit=False)
            myform.save()
            return redirect('/category')
    else:
        form = CategoryForm()
    context={'form':form}
    return render(request,'Category/add_category.html',context)

def edit_Category(request,id):
    post = get_object_or_404(Category ,id=id )
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=post)
        if form.is_valid():
            newform=form.save(commit=False)
            newform.user=request.user
            newform.save()
            return redirect('/category')

    else:
        form = Category(instance=post)
    
    context = {
        'form': form ,
    }

    return render(request,'Category/editcategory.html',context)

def delete_Category(request,id):
    category =Category.objects.get(id=id).delete()

    return redirect('/category')


def Type_list(request):
    ListType = Type.objects.all()

     ##filters##
    my_filter = TypeFilter(request.GET ,queryset=ListType)
    TypeList = my_filter.qs

   

    context = {
        'types':TypeList,
        'my_filter':my_filter
    }
    return render(request,'Type/types.html',context)

def addType(request):
    if request.method=='POST':
        form = TypeForm(request.POST)

        if form.is_valid:
            myform = form.save(commit=False)
            myform.save()
            return redirect('/type')
    else:
        form = TypeForm()
    context={'form':form}
    return render(request,'Type/add_type.html',context)

def edit_Type(request,id):
    post = get_object_or_404(Type ,id=id )
    if request.method=='POST':
        form=TypeForm(request.POST,instance=post)
        if form.is_valid():
            newform=form.save(commit=False)
            newform.save()
            return redirect('/type')

    else:
        form = TypeForm(instance=post)
    
    context = {
        'form': form ,
    }

    return render(request,'Type/edittype.html',context)

def delete_Type(request,id):
    type =Type.objects.get(id=id).delete()

    return redirect('/type')


def Creator_list(request):
    ListCreator = creator.objects.all()

     ##filters##
    my_filter = creatorFilter(request.GET ,queryset=ListCreator)
    CreatorList = my_filter.qs

   

    context = {
        'creators':CreatorList,
        'my_filter':my_filter
    }
    return render(request,'Creator/creators.htm',context)

def addCreator(request):
    if request.method=='POST':
        form = creatorForm(request.POST)

        if form.is_valid:
            myform = form.save(commit=False)
            myform.save()
            return redirect('/creator')
    else:
        form = creatorForm()
    context={'form':form}
    return render(request,'Creator/add_creator.html',context)

def edit_creator(request,id):
    post = get_object_or_404(creator ,id=id )
    if request.method=='POST':
        form=creatorForm(request.POST,instance=post)
        if form.is_valid():
            newform=form.save(commit=False)
            newform.save()
            return redirect('/creator')

    else:
        form = creatorForm(instance=post)
    
    context = {
        'form': form ,
    }

    return render(request,'creator/editcreator.html',context)

def delete_creator(request,id):
    Creator =creator.objects.get(id=id).delete()

    return redirect('/creator')



def Product_list(request):
    ListProduct = Product.objects.filter(active=True)

     ##filters##
    my_filter = ProductFilter(request.GET ,queryset=ListProduct)
    ProductList = my_filter.qs

   

    context = {
        'Products':ProductList,
        'my_filter':my_filter
    }
    return render(request,'Product/products.html',context)

def addProduct(request):
    if request.method=='POST':
        form = ProductForm(request.POST,request.FILES)

        if form.is_valid:
            myform = form.save(commit=False)
            myform.save()
            return redirect('/product')
    else:
        form = ProductForm()
    context={'form':form}
    return render(request,'Product/add_product.html',context)

def edit_Product(request,id):
    post = get_object_or_404(Product ,id=id )
    if request.method=='POST':
        form=ProductForm(request.POST,instance=post)
        if form.is_valid():
            newform=form.save(commit=False)
            newform.save()
            return redirect('/Product')

    else:
        form = ProductForm(instance=post)
    
    context = {
        'form': form ,
    }

    return render(request,'Product/editProduct.html',context)

def delete_Product(request,id):
    product =Product.objects.get(id=id).delete()

    return redirect('/Product')

@login_required
def add_to_cart(request,barcode):
    item = get_object_or_404(Product,barcode=barcode)
    item.quantity -=1
    item.save()
    order_item,created  = OrderItem.objects.get_or_create(
        item=item,
        user =request.user,
        ordered =False
        )
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in order

        if order.items.filter(item__barcode=item.barcode).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request,"this Product quantity was updated")
            return redirect('product:orderSummery')
        else:
            messages.info(request,"this Product was added to your cart")
            order.items.add(order_item)
            return redirect('product:orderSummery')
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
        messages.info(request,"this Product was added to your cart")
    return redirect('product:orderSummery')
@login_required
def remove_from_cart(request,barcode):
    item = get_object_or_404(Product,barcode=barcode)
    item.quantity +=1
    item.save()
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in order

        if order.items.filter(item__barcode=item.barcode).exists():
            order_item=OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered = False
            )[0]
            if order_item.quantity >1.0:
                order_item.quantity -=1
                order_item.save()
                messages.info(request,"this Product was Updated")
            else:
               order.items.remove(order_item)
               order_item.delete()
               messages.info(request,"this Product was removed from your cart")
        else:
            #* adding a message that the user dosn't contain the product
            messages.info(request,"this Product wasn't in your cart")
            print('2')
            return redirect('product:getProduct')
    else:
        #* adding a message that the user dosn't have an order
        messages.info(request,"You don't have an active order")
        print('3')
        return redirect('product:getProduct')

    return redirect('product:orderSummery')

@login_required
def remove_Product_from_cart(request,barcode):
    item = get_object_or_404(Product,barcode=barcode)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in order

        if order.items.filter(item__barcode=item.barcode).exists():
            order_item=OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered = False
            )[0]
            item.quantity += order_item.quantity
            item.save()
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request,"this Product was removed from your cart")
        else:
            #* adding a message that the user dosn't contain the product
            messages.info(request,"this Product wasn't in your cart")
            print('2')
            return redirect('product:getProduct')
    else:
        #* adding a message that the user dosn't have an order
        messages.info(request,"You don't have an active order")
        print('3')
        return redirect('product:getProduct')

    return redirect('product:orderSummery')


class OrderSummery(LoginRequiredMixin , View):
    def get(self, *args, **kwargs):
        try:
            absense=Absense.objects.filter(date=datetime.date.today().strftime("%Y-%m-%d"))
            order ,create= Order.objects.get_or_create(user=self.request.user,ordered=False)
            context={
                'object':order,
                'absense':absense
            }
            return render(self.request,'Product/orderSummery.html',context) 
        except ObjectDoesNotExist:
            messages.ERROR(self.request,"You dont have an active order")
            return redirect('/')
def updateOrder(request,id):
    employe = Employe.objects.get(id=id)
    order = Order.objects.get(user=request.user,ordered=False)  
    order.emp =employe
    order.save()
    return redirect('product:orderSummery')

def checkOut(request):
    order = Order.objects.get(user=request.user,ordered=False) 
    for orderitem in order.items.all():
        orderitem.ordered = True
        orderitem.save()
    
    if order.emp :
        order.ordered =True
        order.save()
        return redirect('product:getProduct')
    else:
        messages.error(request,'You Should select an employe')
    
    return redirect('product:getProduct')



def getOrders(request):
    order = Order.objects.filter(ordered =True)
    x=0
    for ord in order:
        x+=ord.getTotalall()
    
    my_filter = OrderFilter(request.GET ,queryset=order)
    OrderList = my_filter.qs

    context={
        'order':OrderList,
        'allPrice':x,
        'my_filter':my_filter
    }
    return render(request,'Product/getOrders.html',context)

def getDayOrders(request):
    order = Order.objects.filter(ordered =True,order_date__date=datetime.date.today().strftime("%Y-%m-%d"))
    x=0
    for ord in order:
        x+=ord.getTotalall()
    
    my_filter = Order2Filter(request.GET ,queryset=order)
    OrderList = my_filter.qs

    context={
        'order':OrderList,
        'allPrice':x,
        'my_filter':my_filter
    }
    return render(request,'Product/getOrders.html',context)

def remove_Product_from_order(request,barcode,id):
    item = get_object_or_404(Product,barcode=barcode)
    order_qs = Order.objects.filter(user=request.user,ordered=True,id=id)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in order

        if order.items.filter(item__barcode=item.barcode).exists():
            order_item=OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered = True
            )[0]
            item.quantity += order_item.quantity
            item.save()
            order.items.remove(order_item)
            order_item.delete()
            if not order.items.filter(ordered=True).exists():
                order.delete()
            messages.info(request,"this Product was removed from your cart")
        else:
            #* adding a message that the user dosn't contain the product
            messages.info(request,"this Product wasn't in your cart")
            print('2')
            return redirect('product:DayOrders')
    else:
        #* adding a message that the user dosn't have an order
        messages.info(request,"You don't have an active order")
        print('3')
        return redirect('product:DayOrders')

    return redirect('product:DayOrders')

def getDataAndPushInOrder(request):
    if request.POST:
        barcode = request.POST.get('bar')
        item = get_object_or_404(Product,barcode=barcode)
        item.quantity -=1
        item.save()
        order_item,created  = OrderItem.objects.get_or_create(
            item=item,
            user =request.user,
            ordered =False
            )
        order_qs = Order.objects.filter(user=request.user,ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            #check if the order item is in order

            if order.items.filter(item__barcode=item.barcode).exists():
                order_item.quantity +=1
                order_item.save()
                messages.info(request,"this Product quantity was updated")
                return redirect('product:orderSummery')
            else:
                messages.info(request,"this Product was added to your cart")
                order.items.add(order_item)
                return redirect('product:orderSummery')
        else:
            order = Order.objects.create(user=request.user)
            order.items.add(order_item)
            messages.info(request,"this Product was added to your cart")
        return redirect('product:orderSummery')
