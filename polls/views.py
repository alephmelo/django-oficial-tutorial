from django.http import HttpResponse
from .models import Question
from django.shortcuts import render


def index(request):
    lql = Question.objects.order_by('pub_date')[:5]
    context = {'lql': lql}
    return render(request, 'polls/index.html', context)


def detail(request, q_id):
    return HttpResponse('You are in the detail of %s' % q_id)


def results(request, q_id):
    return HttpResponse('You are in the results of %s' % q_id)


def vote(request, q_id):
    return HttpResponse('You are voting on %s' % q_id)
