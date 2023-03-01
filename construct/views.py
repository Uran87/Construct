from django.shortcuts import render
from construct.models import Fence, Requests, Cities
from .forms import ContactForm
from django.views.generic import DetailView, ListView
from Construction import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
# Create your views here.
def my_main_page(request, city='Беларуси'):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    fence = Fence.objects.all()[1]
    city2 = Cities.objects.all()[0]
    city = city2.city_name
    contact_form = ContactForm()
    return render(request, 'construct/main.html', {'form': contact_form,'content': fence, 'city': city})

def fences(request, city='Беларуси'):
    contact_form = ContactForm()
    if is_ajax(request=request):
        form = ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    fences_set = Fence.objects.all()
    city2 = Cities.objects.all()[0]
    city = city2.city_name


    return render(request, 'construct/fences.html', {'form': contact_form,'fences': fences_set, 'city': city})

#@csrf_exempt
def modal_form(request, city='Беларуси'):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponse("gddhgf")


def contact(request):
    form = ContactForm()

    # if request.method == 'POST':
    #     form = ContactModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('contact')
    if request.is_ajax():
        form = ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'construct/fences.html', {'form': form})


def main_page(request):
    fence = Fence.objects.all()[1]
    return render(request, 'construct/home.html', {'foo': fence})

"""def fences(request, slug):
    fence = Fence.objects.all()[1]
    slug = Cities.objects.get(url='slug')
    return render(request, 'construct/fences.html', {'foo': slug})"""




class CitiesDetailView(DetailView):

    """Полное описание фильма"""
    model = Cities
    slug_field = "slug_city"
    template_name = "construct/fences.html"