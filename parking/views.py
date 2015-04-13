from django.shortcuts import render
from parking.models import rack, review

# Create your views here.
def home (request):
    return render(request, "base.html", {
        'racks': rack.objects.all()

    })
