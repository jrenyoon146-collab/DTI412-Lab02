from django.shortcuts import render
from .models import Course

def home_view(request):
    courses = Course.objects.all()
    return render(request, 'catalog/home.html', {
        'courses': courses
    })

def course_list_view(request):
    courses = Course.objects.all()
    return render(request, 'catalog/course_list.html', {
        'courses': courses
    })

def course_detail_view(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'catalog/course_detail.html', {
        'course': course
    })

def inquiry_view(request):
    return render(request, 'catalog/inquiry.html')