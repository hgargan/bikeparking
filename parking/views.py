from django.shortcuts import render, get_object_or_404 
from parking.models import Rack
from parking.models import Review
from parking.models import rackForm, reviewForm

# Create your views here.
def home (request):
    return render(request, "parking/home.html")


def find (request):
    return render(request, "parking/map.html", {
        'racks': Rack.objects.all()
    })

def detail (request, pk):
    rack = get_object_or_404(Rack, id=pk)
    reviews = rack.review_set.all()
    return render(request, "parking/rack.html", {
        'rack': rack,
        'reviews': reviews
    })

def review(request):
    form2 = reviewForm(request.POST or None)
    if form2.is_valid():
        form2.save()
    return render(request, "parking/review.html", {
            'form2': form2
    })

def submit(request):
    form = rackForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "parking/submit.html", {
            'form': form 
    })


