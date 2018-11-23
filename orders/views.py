from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderItem, Order
from cart.cart import Cart
from accounts.models import MyUser
def order_create(request):
    cart = Cart(request)
    current_user = request.user
    order = get_object_or_404(Order, account_id=current_user.id)
    print(order)
    if request.method == 'POST':
        if order is None:
            return redirect('')
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        return render(request, 'orders/created.html')
    else:
        context = {
            'order': order,
        }
    return render(request, 'orders/create.html', context)

def order_more(request):
    if request.method == 'POST':
        current_user = request.user
        user = current_user
        address = request.POST["address"]
        postalcode = request.POST["postalcode"]
        city = request.POST["city"]
        Order.objects.create(
            account = user,
            address = address,
            postal_code = postalcode,
            city = city
        )
        return redirect('orders:order_create')
    else:
        return render(request, 'orders/fillout.html')
