from django.shortcuts import get_object_or_404, redirect, render
from .forms import CategoryForm,ColorForm,TypeForm,creatorForm
from .models import Category,Color,Type,creator
from .filters import ColorFilter,CategoryFilter,TypeFilter,creatorFilter
from product.models import Product
from product.filters import ProductFilter
from product.forms import ProductForm

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
