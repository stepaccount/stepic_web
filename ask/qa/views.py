from django.shortcuts import render
from django.http import HttpResponse 
from django.http import Http404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from .models import *

@require_GET
def test(request, *args):
    return HttpResponse('OK')

@require_GET
def mainroot(request, *args):
    try:
        page = int(request.GET.get('page', 1))
        limit = 10
        questions = Question.objects.new()
    except Exception:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'main_page.html', {'questions': page.object_list, 'paginator': paginator, 'page': page,})

@require_GET
def popular(request, *args):
    try:
        page = int(request.GET.get('page', 1))
        limit = 10
        pop_questions = Question.objects.popular() #QuerySet
    except Exception:
        raise Http404
    paginator = Paginator(pop_questions, limit)
    paginator.baseurl = '/popular/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'pop_page.html', {'questions': page.object_list, 'paginator': paginator, 'page': page,})
    
@require_GET
def question(request, id):
    try:
        q_num = int(id)
        user_question = Question.objects.get(pk = q_num)
    except Question.DoesNotExist:
        raise Http404
    except Exception:
        raise Http404
    try:
        answers = Answer.objects.filter(question = user_question)[:]
    except Answer.DoesNotExists:
        answers = []
    return render(request, 'question_page.html', {'question': user_question, 'answers': answers,})
