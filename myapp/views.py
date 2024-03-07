from django.shortcuts import render, HttpResponseRedirect
from .currencyapi import CurrencyAPI
from .models import Currency

# Create your views here.
def home(request):
    currencyAPI = CurrencyAPI()
    items = currencyAPI.get_currencies()
    base_curr = None
    curr_to = None
    amount = None

    if request.method == "POST":
        currency_form = Currency(request.POST)

        if currency_form.is_valid():
            base_curr = currency_form.data["base_curr"]
            curr_to = currency_form.data["curr_to"]
            amount = currency_form.data["quantity"]

        conv_amount = currencyAPI.get_conversion(base_curr, curr_to, amount)
    else:
        currency_form = Currency()
        conv_amount = None

    return render(request, 'base.html', {"currencies": items, 
                                         "form_data": currency_form.data,
                                         "conv_amount": conv_amount})



