from django.shortcuts import render, redirect
from . models import Donation

# Create your views here.
def home(request):
   return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def donate(request):
    if request.method == "POST":
        fname = request.POST.get('fname',False)
        lname = request.POST.get('lname',False)
        mail = request.POST.get('mail',False)
        code = int(request.POST.get('code',False))
        number = int(request.POST.get('number',False))
        street_address = request.POST.get('street_address',False)
        street_address_2 = request.POST.get('street_address_2',False)
        city = request.POST.get('city',False)
        state = request.POST.get('state',False)
        pincode = int(request.POST.get('pincode',False))
        amount = int(request.POST.get('amount',False))
        mop = request.POST.get('mop',False)
        account_no = int(request.POST.get('account_no',False))
        same = request.POST.get('same',False)
        confirm = int(request.POST.get('confirm',False))
        pre = Donation(fname=str(fname),lname=str(lname),mail=str(mail),code=str(code),
                       number=str(number),street_address=str(street_address),street_address_2=str(street_address_2),
                       city=str(city),state=str(state),pincode=str(pincode),amount=str(amount),mop=str(mop),
                       account_no=str(account_no),same=str(same),confirm=str(confirm)) #ORM
        pre.save()
        print(request.POST)
    return render(request, "donate.html", {})
    # return redirect('donation')

def faq(request):
    return render(request, "faq.html", {})

def contact(request):
    return render(request, "contact.html", {})