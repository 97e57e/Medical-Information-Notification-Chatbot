from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def main(request):

    template = loader.get_template('polls/main.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))


def login(request):

    template = loader.get_template('polls/login.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def qna(request):

    template = loader.get_template('polls/qna.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
