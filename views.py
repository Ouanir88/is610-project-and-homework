from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import BakedGood, BakedGoodForm
from .forms import NameForm
from django.urls import reverse

def index(request):
    baked_goods = BakedGood.objects.all()
    context = {'baked_goods': baked_goods}
    return render (request, 'app/extend.html', context)

def another(request):
    return HttpResponse("Hello from the other world")


def mysite(request):
    context = {'message': " Hooray, you entered mysite successfully!" }
    return render (request, 'app/mysite.html', context)
       
def Ouanir(request):
    if request.method == 'POST':
        form = BakedGoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = BakedGoodForm()

    return render(request, 'app/Ouanir.html', {'form': form})