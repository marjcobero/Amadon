from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request, order_id):
    oneOrder = Order.objects.get(id= order_id)
    num_of_items = oneOrder.quantity_ordered
    price = oneOrder.total_price
    total_charge = num_of_items * price
    all_orders = Order.objects.all()
    sum = 0
    for order in all_orders:
        sum += order.total_price 
    context = {
        'orders': num_of_items,
        'total' : total_charge,
        'bill' : sum,
    }
    return render(request, 'store/checkout.html', context)

def purchase(request):
    if request.method == "POST":
        num_of_items = int(request.POST['quantity'])
        price = Product.objects.get(id=request.POST['product_id']).price
        price = int(price)
        total_charge = num_of_items * price
        print('Charging credit card...')
        oneOrder = Order.objects.create(quantity_ordered=num_of_items, total_price= total_charge)
        id = oneOrder.id
        return redirect(f'/checkout/{id}')
    return redirect('/')

def new(request):
    Product.objects.create(description=request.POST['description'],price=request.POST['price'])
    return redirect("/")

