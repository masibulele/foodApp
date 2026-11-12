from django.shortcuts import render , redirect
from . import models
from .form import ItemForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request):
    fooditems = models.Item.objects.all()
    context = {
        'items_list':fooditems
    }

    return render(request,'foodApp/index.html', context=context)

# create details view
def details(request,id):
    currentItem =  models.Item.objects.get(pk=id)
    print(currentItem)
    context = {
        'item' : currentItem
    }
    return render(request,'foodApp/details.html', context= context)


# create additional product

def create_item(request):
    # create blank form
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foodApp:index')

    form = ItemForm()
    context ={
        'form':form
    }
    return render(request,'foodApp/add.html',context)

def edit_item(request, id):

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foodApp:index')


    currentItem = models.Item.objects.get(id=id)
    form = ItemForm(instance=currentItem)
    context ={
        'form': form
    }


    return render(request, 'foodApp/edit.html',context)


def delete_item(request, id):
    if request.method == "POST":
        currentItem = models.Item.objects.get(id=id)
        currentItem.delete()
        return redirect("foodApp:index")

    return render(request, 'foodApp/delete.html')


