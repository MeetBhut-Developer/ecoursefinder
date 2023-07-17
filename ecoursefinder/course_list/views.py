from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Master_Courses
from django.core.paginator import Paginator
# Create your views here.

def course_list(request):
    courses = Master_Courses.objects.all()
    paginator = Paginator(courses, 12)  # Show 12 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'course.html', {'page_obj': page_obj})

def under_construction(request):
    return render(request,'under_construction.html')

def index(request):
    courses = Master_Courses.objects.all()
    paginator = Paginator(courses, 3)  # Show 12 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})