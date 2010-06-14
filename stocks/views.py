from django.shortcuts import render_to_response
from django.template import RequestContext

from stocks.forms import StockForm


def index(request):
    data = {}

    return render_to_response(
        'stocks/index.html',
        data,
        context_instance=RequestContext(request),
    )

def create(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
    else:
        form = StockForm()

    data = {
        'form': form,
    }

    return render_to_response(
        'stocks/create.html',
        data,
        context_instance=RequestContext(request),
    )

def update(request):
    data = {}

    return render_to_response(
        'stocks/update.html',
        data,
        context_instance=RequestContext(request),
    )
