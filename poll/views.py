import io
import reportlab
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.shortcuts import render
from .forms import PersonForm
from .models import Person


# Create your views here.


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context['form'] = form
    return render(request, "poll/create_view.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Person.objects.all()

    return render(request, "poll/list_view.html", context)


# after updating it will redirect to detail_View


def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Person.objects.get(id=id)

    return render(request, "poll/detail_view.html", context)

# update view for details


def update_view(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Person, id=id)

    # pass the object as instance in form
    form = PersonForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "poll/update_view.html", context)


# delete view for details
def delete_view(request, id):
    context = {}

    obj = get_object_or_404(Person, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "poll/delete_view.html", context)


def export_to_pdf(request, id):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    person_objt = Person.objects.get(pk=id)

    p.drawCentredString(250, 745, 'Nombre: ' + str(person_objt.name))
    p.drawCentredString(250, 730, 'Edad: ' + str(person_objt.age))
    p.drawCentredString(250, 715, 'Sexo: ' + str(person_objt.sex))
    p.drawCentredString(250, 700, 'Nivel Educacional: ' +
                        str(person_objt.education_level))
    p.drawCentredString(250, 685, 'Peso corporal: ' +
                        str(person_objt.body_weight))
    p.drawCentredString(250, 670, 'Informacion: ' +
                        str(person_objt.personal_information))

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='document_poll.pdf')
