from django.shortcuts import render, get_object_or_404 
from parking.models import rack as Rack
from parking.models import review as Review
from parking.models import rackForm, reviewForm

# Create your views here.
def home (request):
    form = rackForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, "rack.html", {
        })
    return render(request, "base.html", {
        'racks': Rack.objects.all(),
        'form': form    
    })


def find (request):
    return render(request, "find.html", {
        'racks': Rack.objects.all()
    })

def detail (request, pk):
    rack = get_object_or_404(Rack, id=pk)
    reviews = rack.review_set.all()
    return render(request, "rack.html", {
        'rack': rack,
        'reviews': reviews
    })

