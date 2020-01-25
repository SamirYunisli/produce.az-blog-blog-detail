
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Event
from django.db.models import Q
# Create your views here.

def create_event(request):
    event_list = Event.objects.all()

    if request.method == 'POST':
        search = request.POST.get('search')
        event_list = Event.objects.filter(Q(title__icontains=search) | Q(text__icontains=search) | Q(description__icontains=search))

    paginator = Paginator(event_list, 2)

    first_count = Event.objects.filter(test_date__year = 2020, test_date__month = 1).count()
    second_count = Event.objects.filter(test_date__year = 2019, test_date__month = 11).count()
    third_count = Event.objects.filter(test_date__year = 2019, test_date__month = 12).count()


    page = request.GET.get('page')
    events = paginator.get_page(page)

    context = {
        'events': events,
        'first_count': first_count,
        'second_count': second_count,
        'third_count': third_count,
    }
    return render(request, 'event.html', context)


def get_event_detail(request, id):
    event = Event.objects.get(id=id)

    context = {
        'event': event
    }
    return render(request, 'event-detail.html', context)

def get_archieve(request, year, month):
    event_list = Event.objects.filter(test_date__year = year, test_date__month = month)

    if request.method == 'POST':
        search = request.POST.get('search')
        event_list = Event.objects.filter(Q(title__icontains=search) | Q(text__icontains=search) | Q(description__icontains=search))
    
    first_count = Event.objects.filter(test_date__year = 2020, test_date__month = 1).count()
    second_count = Event.objects.filter(test_date__year = 2019, test_date__month = 11).count()
    third_count = Event.objects.filter(test_date__year = 2019, test_date__month = 12).count()

    paginator = Paginator(event_list, 2)

    page = request.GET.get('page')
    events = paginator.get_page(page)

    context = {
        'events': events,
        'first_count': first_count,
        'second_count': second_count,
        'third_count': third_count,
    }
    return render(request, 'event.html', context)
