from django.shortcuts import render
from .models import Product, Lesson, Group, Student


def index(request):
    products = Product.objects.all()
    lessons = Lesson.objects.all()
    groups = Group.objects.all()
    students = Student.objects.all()
    return render(
        request,
        'education_system/index.html',
        {'title': 'ЯЗЫКИ ПРОГРАММИРОВАНИЯ',
        'products': products,
        'lessons': lessons,
        'groups': groups,
        'students': students}
        )

def about(request):
    return render(request, 'education_system/about.html')