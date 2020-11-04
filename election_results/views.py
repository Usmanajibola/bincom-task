from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'home.html')

def units(request):
    units = Polling_Unit.objects.all()
    
    context = {'units':units}
    return render(request, 'polling_units.html', context)


def unit(request):
    if request.method == 'POST':
        unit_id = request.POST.get('unit_name')
        unit = Polling_Unit.objects.get(uniqueid=unit_id)
        results = Announced_Pu_Results.objects.filter(polling_unit_uniqueid=unit.uniqueid)
        context = {'results':results}

        return render(request, 'polling_unit.html', context)

def lgas(request):
    lgas = Lga.objects.all()

    context = {"lgas":lgas}

    return render(request, 'local_governments.html', context)


def lga(request):
    if request.method == 'POST':
        lga_id = request.POST.get('lga_name')
        polling_units = Polling_Unit.objects.filter(lga_id=lga_id)
        arr = []
        for p in polling_units:
            results = Announced_Pu_Results.objects.filter(polling_unit_uniqueid=p.uniqueid)
            arr.append(results)
        if not arr:
            return HttpResponse('<h2>Result not found ...</h2>')
        results = [0] * len(arr[0])
        final_result = []

       

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                results[j] += arr[i][j].party_score

        for i in range(len(arr[0])):
            final_result.append((arr[0][i].party_abbreviation, results[i]))

        
        final_result = dict(final_result)
        context = {'results':final_result}

        return render(request, 'local_government.html', context)

def all_parties(request):
    units = Polling_Unit.objects.all()
    
    context = {'units':units}
    return render(request, 'all_parties.html', context)

def unit_sum(request):
    if request.method == 'POST':
        unit_id = request.POST.get('unit_name')
        unit = Polling_Unit.objects.get(uniqueid=unit_id)
        results = Announced_Pu_Results.objects.filter(polling_unit_uniqueid=unit.uniqueid)
        if results.exists() == False:
            return HttpResponse('<h2>Result not found...</h2>')
        total = 0
        for i in results:
            total+=i.party_score

        context = {"unit":unit, "total":total}

        return render(request, 'polling_unit_sum.html', context)


