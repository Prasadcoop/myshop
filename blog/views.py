from django.shortcuts import render
from .models import Product, Phone1, Order, OrderUpdate
from math import ceil
import logging
logger =logging.getLogger(__name__)
from django.http import HttpResponse
import json
#def index(request):
#( products =Product.objects.all()
 #  print(products)
 #  n= len(products)
 #  nSlides =n//4 + ceil((n//4)+(n//4))
 #  params ={'no_of slides': nSlides, 'range': range(nSlides), 'product': products }

   #return render(request, 'blog/index.html', params))

def about(request):
    return render(request, 'blog/about.html')

def phone1(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        phone1= Phone1(name=name, email=email, phone=phone, desc=desc)
        phone1.save()
    return render(request, 'blog/contact.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'blog/tracker.html')
def search(request):
    return render(request, 'blog/search.html')

def productView(request, myid):
    product = Product.objects.filter(id=myid)

    return render(request, 'blog/product.html',{'product': product[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        adress = request.POST.get('adress', '')
        adress2 = request.POST.get('adress2', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        pin_code = request.POST.get('pin_code', '')
        order = Order(items_json=items_json, name=name, email=email, phone=phone, adress=adress, adress2=adress2, state=state, city=city, pin_code=pin_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="the order has been place")
        update.save()
        thank = True
        id = order.order_id
        return render(request,'blog/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'blog/checkout.html')

def support(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    #allProds = [[products, range(1, nSlides), nSlides],
     #           [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'blog/support.html', params)

def footer(request):

    return render(request, 'blog/footer.html')
