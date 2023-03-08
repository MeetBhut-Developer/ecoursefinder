# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def course_list(request):
    course_template = loader.get_template('course.html')
    return HttpResponse(course_template.render())