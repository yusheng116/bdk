from django.shortcuts import render



def order(request):
    '''
    Render the order page
    '''
    return render(request, 'order/order.html')
 