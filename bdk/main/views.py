from django.shortcuts import render

def main(request):
    '''
    Render the main page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'main/main.html', context)
def shoes1(request):
    '''
    Render the about page
    '''
    return render(request, 'main/shoes1.html')
def shoes2(request):
    '''
    Render the about page
    '''
    return render(request, 'main/shoes2.html')
def shoes3(request):
    '''
    Render the about page
    '''
    return render(request, 'main/shoes3.html')
    
