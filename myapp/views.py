from django.shortcuts import render, redirect
from . models import Donation, Membership, Feedback

# Create your views here.
def home(request):
   return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def donate(request):
    if request.method == "POST":
        try:
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
            amount = float(request.POST.get('amount',False))
            mop = request.POST.get('mop',False)
            account_no = int(request.POST.get('account_no',False))
            same = request.POST.get('same',False)
            confirm = request.POST.get('confirm',False)
            if confirm == "on":
                confirm = True
            else:
                confirm = False
            pre = Donation(fname=str(fname),lname=str(lname),mail=str(mail),code=str(code),
                           number=str(number),street_address=str(street_address),street_address_2=str(street_address_2),
                           city=str(city),state=str(state),pincode=str(pincode),amount=str(amount),mop=str(mop),
                           account_no=str(account_no),same=str(same),confirm=str(confirm)) #ORM
            pre.save()
            # print(request.POST)
        except Exception as e:
            print(e)
    return render(request, "donate.html", {})
    # return redirect('donation')

def join(request):
    if request.method == "POST":
        try:
            fname = request.POST.get('fname', False)
            lname = request.POST.get('lname', False)
            same = request.POST.get('same', False)
            dob = request.POST.get('dob', False)
            mail = request.POST.get('mail', False)
            code = int(request.POST.get('code', False))
            number = int(request.POST.get('number', False))
            street_address = request.POST.get('street_address', False)
            street_address_2 = request.POST.get('street_address_2', False)
            city = request.POST.get('city', False)
            state = request.POST.get('state', False)
            pincode = int(request.POST.get('pincode', False))
            mp = request.POST.get('mp', False)
            text = request.POST.get('text', False)
            confirm = request.POST.get('confirm', False)
            if confirm == "on":
                confirm = True
            else:
                confirm = False

            pre1 = Membership(fname=str(fname),lname=str(lname),same=str(same),dob=str(dob),mail=str(mail),code=str(code),
                              number=str(number),street_address=str(street_address),street_address_2=str(street_address_2),
                              city=str(city),state=str(state),pincode=str(pincode),mp=str(mp),text=str(text),confirm=str(confirm))  # ORM
            pre1.save()
        except Exception as e:
            print(e)
    return render(request, "join.html", {})

def faq(request):
    return render(request, "faq.html", {})

def feedback(request):
    if request.method == "POST":
        try:
            fname = request.POST.get('fname', False)
            lname = request.POST.get('lname', False)
            mail = request.POST.get('mail', False)
            text = request.POST.get('text', False)
            pre2 = Feedback(fname=str(fname),lname=str(lname),mail=str(mail),text=str(text))
            pre2.save()
        except Exception as e:
            print(e)
    return render(request, "feedback.html", {})

def contact(request):
    return render(request, "contact.html", {})
