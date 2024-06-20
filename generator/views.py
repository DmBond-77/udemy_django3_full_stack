from django.shortcuts import render
# from django.http import HttpResponse
import string
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')

def password(request):
    letters = list(string.ascii_lowercase)

    the_password = ''
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        letters.extend(list(string.ascii_uppercase))

    if request.GET.get('numbers'):
        letters.extend(list(string.digits))

    if request.GET.get('special'):
        letters.extend(string.punctuation)

    the_password = ''.join(random.choice(letters) for _ in range(length))

    return render(request, 'generator/password.html', {'password': the_password, 'request': request, 'letters': letters})