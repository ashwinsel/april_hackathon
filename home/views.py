from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')

def contact(request):
    return render(request, 'home/contact.html')

def aboutUs(request):
    return render(request, 'home/about_us.html')

def endometriosis(request):
    return render(request, 'home/endometriosis.html')

def menopause(request):
    return render(request, 'home/menopause.html')

def notBeingHeard(request):
    return render(request, 'home/not_being_heard.html')




