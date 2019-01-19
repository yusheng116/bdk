from django.shortcuts import render
from order.forms import OrderForm



def Order(request):
    '''
    Render the order page
    '''
    template='order/order.html'
    if request.method =='GET':
        return render(request, template,{'orderForm':OrderForm()})
    
    
    orderForm = OrderForm(request.POST)
    if not orderForm.is_valid():
        return render(request, template, {'orderForm':OrderForm})
    orderForm.save()
    return render(request, 'main/main.html')