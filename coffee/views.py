from datetime import datetime, timezone
from django.shortcuts import render, redirect
from django.urls import reverse

from coffee.forms import GiftTo
from coffee.models import Coffee


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        pendient_coffees = Coffee.objects.all().filter(time__isnull=True)
        delivered_coffees = Coffee.objects.all().exclude(giftTo="")
        context = {
            "pendient_coffees": pendient_coffees,
            "delivered_coffees": delivered_coffees,
            "session": request.user
        }
        return render(request, "home.html", context)
    else : return redirect('account/login')


def add(request):
    coffee = Coffee(giftTo='', username=request.user.username)
    coffee.save()
    return redirect('/')


def gift_to(request):
    if request.method == "POST":
        form = request.POST
        coffeeToGift = Coffee.objects.filter(giftTo__exact='').first()
        coffeeToGift.giftTo = form.get('giftTo')
        coffeeToGift.time = datetime.now(timezone.utc)
        if coffeeToGift.can_be_gifted(coffeeToGift):
            coffeeToGift.save()
            return home(request)
        else:
            context = {
                'to': form.get('giftTo')
            }
            return render(request, 'gift_to.html', context)
    else:
        context = {}
        context['form'] = GiftTo()
        return render(request, 'gift_to.html', context)
