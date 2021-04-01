from django.db import models

# Create your models here.

class Donation(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    number = models.CharField(max_length=11)
    street_address = models.CharField(max_length=100)
    street_address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    amount = models.CharField(max_length=10)
    mop_choices = (
        ("cc", "Credit Card"),
        ("ot", "Online Banking"),
        ("pp", "PayPal"),
    )
    mop = models.CharField(choices=mop_choices, default="", max_length=3)
    account_no = models.CharField(max_length=18)
    mail_rec = (
        ("yes", "Yes"),
        ("no", "No"),
    )
    same = models.CharField(choices=mail_rec, max_length=3)
    confirm = models.BooleanField(default=False)
    # result = models.CharField(max_length=50)
