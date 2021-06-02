from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Shows
from time import strftime, strptime
from datetime import date, datetime

#index route automatically redirects to the main route "/shows"
def index(request):
    return redirect("/shows")

#Main route renders a list of all records from model "shows" in database. 
def main(request):
    context = {
        "all_shows": Shows.objects.all(),
    }
    print(context)
    return render(request, "main.html", context)

#route "shows/new" renders a form to add new shows.
def newform(request):
    return render(request, "new_form.html")

#route "shows/create" takes POST data from new form to create new record to model "shows" in database.
def create(request):
    #validation checks for errors first
    errors = Shows.objects.basic_validator(request.POST)
    #if length from dictionary is greater than 0, then display error message from model manager.
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    #if no errors are found then take POST data to create new record
    else: 
        new_show = Shows.objects.create(title= request.POST['title'], network= request.POST['network'], release_date= request.POST['releasedate'], desc= request.POST['desc'])
        print(new_show.id)
        return redirect(f"/shows/{new_show.id}")

#route /shows/id displays data for record selected.
def show_info(request, show_id):
    show = Shows.objects.get(id=show_id)
    #format time for field to display as M/DD/YYYY
    release_format = show.release_date.strftime('%B %d, %Y')
    context = {
        "release_date_format": release_format,
        "this_show": show,
    }
    return render(request, "show_info.html", context)

#route /id/edit displays form with current data of record in input fields. 
def edit(request, show_id):
    show = Shows.objects.get(id=show_id)
    release_format = show.release_date.strftime('%m/%d/%Y')
    context = {
        "this_show": show, 
        "release_date_format": release_format
    }
    return render(request, "edit_form.html",context)

#route /shows/id/update takes data from POST and updates record
def update(request, show_id):
    #validations to check for errors.  If errors are shown, then display error messages
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/{show_id}/edit")
    else:
        input_date= request.POST['releasedate']
        current_date= datetime.strptime(input_date, '%m/%d/%Y')
        format_date= current_date.strftime('%Y-%m-%d')
        update = Shows.objects.get(id= show_id)
        update.title = request.POST['title']
        update.network = request.POST['network']
        update.release_date = format_date
        update.desc = request.POST['desc']
        update.save()
        return redirect(f"/shows/{show_id}")

#route shows/id/destroy deletes record
def delete(request, show_id):
    show_to_delete = Shows.objects.get(id= show_id)
    show_to_delete.delete()
    return redirect("/shows")


# Create your views here.
