from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from datetime import datetime, time, timezone
from time import gmtime, strftime
from django.contrib import messages

# 1. # GET /shows/new
def addNewShow(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'addNewShow.html', context)

#2. # POST /shows/create
def createNewShow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect(f'/shows/{show.id}')


# 3. GET shows/id
def tvShow(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'tvShow.html', context)


# 4 GET /shows ------ 'show' was 'shows'
def allShows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'allShows.html', context)


# 5 GET /shows/<id>
def editShow(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'editShow.html', context)


# 6 POST shows/<id>/update
def updateShow(request, id):
        print("Request", request)
    print(request.POST)
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect(f'/shows/{id}')


# 7 POST shows/<id>/destroy
def deleteShow(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')


# 8 POST /shows Root Rout redirects to /shows
def index(request):
    return redirect('/shows')