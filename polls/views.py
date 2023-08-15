from django.shortcuts import render
from .models import Question

from django.http import HttpResponse


# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()
    try:
        print("request Meta --> \n", request.body)
        output = ",".join([q.question_text for q in latest_question_list])
    except Exception as e:
        return HttpResponse("no data found")
    else:
        return render(request, "polls/index.html", {"data": output})


def detail(request, question_id):
    print("request header printed", request)
    return HttpResponse("hello this is question %s" % question_id)


def result(request, question_id):
    return HttpResponse("result of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("you casted vote for question %s" % question_id)
