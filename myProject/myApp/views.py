from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import Course

def index(request):
    course_list = Course.objects.order_by('-title', 'startdate', 'description')

    context_dict = {}
    context_dict['courses'] = course_list
    return render(request, 'myApp/course.html', context=context_dict)

