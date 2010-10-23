from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext

from customers.models import Customer
from stocks.models import Stock
from utils.constants import CUSTOMERS_APP, STOCKS_APP


def index(request):
    data = {}

    return render_to_response(
        'home/index.html',
        data,
        context_instance=RequestContext(request),
    )


def search(request):
    current_app = request.GET.get('current-app', '')
    q = request.GET.get('q', '')

    if current_app == CUSTOMERS_APP:
        results = Customer.objects.filter(
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q) |
            Q(company_name__icontains=q)
        )
    elif current_app == STOCKS_APP:
        stocks = Stock.objects.filter(
            Q(category__code__istartswith=q) |
            Q(description__istartswith=q)
        )

        data = {
            'stocks': stocks,
        }

        return render_to_response(
            'stocks/index.html',
            data,
            context_instance=RequestContext(request),
        )
    else:
        results = []

    data = {
        'results': results,
    }

    return render_to_response(
        'home/search.html',
        data,
        context_instance=RequestContext(request),
    )
