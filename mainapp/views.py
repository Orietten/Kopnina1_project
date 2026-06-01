from django.shortcuts import render

import math
from django.shortcuts import render

# Данные для страницы "Образовательная программа"
def get_education_context():
    return {
        'student': {
            'full_name': 'Копнина Мария Евгеньевна',
            'email': 'maevkopnina@edu.hse.com',
            'phone': '+7 (999) 123-45-67',
        },
        'program': {
            'name': 'Экономика и статистика',
            'description': 'это возможность получить самую востребованную профессию экономиста-статистика, который сможет в огромном море информации выполнять функции лоцмана для крупного бизнеса и делать точные прогнозы на основе анализа собранной им информации.'
        },
        'head': {
            'full_name': 'Сиротин Вячеслав Павлович',
            'email': 'sirotin@university.ru',
        },
        'manager': {
            'full_name': 'Лосева Екатерина',
            'email': 'loseva@university.ru',
        },
        'classmates': [
            {'name': 'Воропаев Иван Андреевич', 'email': 'ivanvoropaev@example.com', 'phone': '+7 (111) 111-11-11'},
            {'name': 'Петр Смирнов', 'email': 'petr@example.com', 'phone': '+7 (222) 222-22-22'},
            {'name': 'Елена Васильева', 'email': 'elena@example.com', 'phone': '+7 (333) 333-33-33'},
        ]
    }

def index(request):
    return render(request, 'index.html')

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')

def page4(request):
    return render(request, 'page4.html')

def education(request):
    context = get_education_context()
    return render(request, 'education.html', context)

def task_solution(request):
    context = {}
    if request.method == 'POST':
        try:
            s = float(request.POST.get('area', 0))
            r = float(request.POST.get('radius', 0))
            k = float(request.POST.get('passage', 0))
            if s <= 0 or r <= 0 or k <= 0:
                context['error'] = "Все значения должны быть положительными"
            else:
                a = math.sqrt(s)
                r_max = a / 2 - k
                result = r <= r_max
                context.update({
                    's_value': s, 'r_value': r, 'k_value': k,
                    'a_value': a, 'r_max': r_max, 'result': result,
                })
        except ValueError:
            context['error'] = "Введите корректные числа"
    return render(request, 'task_solution.html', context)
