from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm


def Show_View(request):
    template_name = 'OrderList/Show.html'
    obj = Order.objects.all()
    context = {'obj': obj}
    return render(request, template_name, context)


def Add_View(request):
    if request.method == "GET":
        template_name = 'OrderList/Add.html'
        form = OrderForm()
        context = {'form': form}
        return render(request, template_name, context)
    elif request.method == "POST":
        filled_form = OrderForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('/order/show/')


def Update_view(request, i):
    if request.method == "GET":
        template_name = 'OrderList/Add.html'
        Order_obj = Order.objects.get(id=i)
        form = OrderForm(instance=Order_obj)
        context = {'form': form}
        return render(request, template_name, context)
    elif request.method == "POST":
        Order_obj = Order.objects.get(id=i)
        filled_form = OrderForm(request.POST, instance=Order_obj)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('/order/show/')


def Delete_view(request, i):
    Order_obj = Order.objects.get(id=i)
    Order_obj.delete()
    return redirect('/order/show/')
