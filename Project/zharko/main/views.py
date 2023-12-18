from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Catalog, Review
from .forms import AddReview, Request
from .telegram import Telegram
import time

# Create your views here.

def formtg(request):
    if request.method == 'POST':
        form = Request(request.POST)
        if form.is_valid():
            user_entry = Telegram()
            user_entry.name = form.cleaned_data['name']
            user_entry.phone = form.cleaned_data['phone']
            user_entry.send_message()
            return form
        else:
            pass
    else:
        form = Request()
    return form

def home(request):
    tg_form = formtg(request)
    return render(request, 'main/index.html', {'form':tg_form})

def catalog(request):
    tg_form = formtg(request)
    products = Catalog.objects.all()
    return render(request, 'main/catalog.html', {'products':products, 'form':tg_form}) 

def product(request, prod_id):
    tg_form = formtg(request)
    try:
        p = Catalog.objects.get(id=prod_id)
        return render(request, 'main/product.html', {'p':p, 'form':tg_form})
    except:
        return HttpResponseNotFound()

def reviews(request):
    tg_form = formtg(request)
    if request.method == 'POST':
        form = AddReview(request.POST, request.FILES)

        if form.is_valid():
            reviews_entry = Review()
            reviews_entry.author = form.cleaned_data['author']
            reviews_entry.email = form.cleaned_data['email']
            reviews_entry.comment = form.cleaned_data['comment']
            reviews_entry.image = form.cleaned_data['image']
            reviews_entry.date = time.strftime("%H:%M, %d.%m.%Y")
            reviews_entry.save()
            return redirect('reviews')
        else:
            pass
    else:
        form = AddReview()

    forms = Review.objects.all().order_by('-id') 
    return render(request, 'main/reviews.html', {'form_rew':form, 'forms':forms, 'form':tg_form})

def about(request):
    tg_form = formtg(request)
    return render(request, 'main/about.html', {'form':tg_form})