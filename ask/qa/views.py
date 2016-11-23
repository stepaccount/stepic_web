from django.shortcuts import render
from django.http import HttpResponse 
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from .models import *
from .forms import *

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


def question(request, id):
    #Test error
    if request.method == "POST":
        return HttpResponse('OK')
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
    answer_form = AnswerForm(initial = {'question': q_num, 'hidden_id': q_num, }) 
    return render(request, 'question_page.html', {'question': user_question, 'answers': answers, 'form': answer_form, })

def new_ask(request):
    if request.method == 'POST':
        #POST
        ask_form = AskForm(request.POST)
        if ask_form.is_valid():
            new_que = ask_form.save()
            return HttpResponseRedirect(new_que.get_absolute_url())
    else:
        #GET
        ask_form = AskForm() #Blank form
    return render(request, 'ask_page.html', {'form': ask_form})

@require_POST
def add_answer(request):
    answer_form = AnswerForm(request.POST)
    if answer_form.is_valid():
        try:
            q_num = int(answer_form.cleaned_data['hidden_id'])
            #user_question = Question.objects.get(pk = q_num)
        except Exception:
            raise Http404
        new_ans = answer_form.save()
        return HttpResponseRedirect(new_ans.question.get_absolute_url())
    else:
        try:
            q_num = int(answer_form.cleaned_data['hidden_id'])
            user_question = Question.objects.get(pk = q_num)
        except Exception:
            raise Http404
        return HttpResponseRedirect(user_question.get_absolute_url())
