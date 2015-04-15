from django.shortcuts import render
from parking.models import rack, review, rackForm, reviewForm

# Create your views here.
def home (request):
    form = rackForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, "rack.html", {
        })


        
    return render(request, "base.html", {
        'racks': rack.objects.all(),
        'form': form

    })

