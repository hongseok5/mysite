from django.shortcuts import render, get_object_or_404
from polls.models import Question
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import  reverse
from polls.models import Choice, Question


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'lastest_question_list': latest_question_list }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# 폼으로부터 수신한 POST 데이터를 처리하는 함수
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다.
        return render(request, 'poll/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()

        # 포스트 데이터를 정상적으로 처리하였으면,
        # 항상 HttpResponseRedirect 를 반환하여 리다이렉션 처리함

        return HttpResponseRedirect(reverse('polls:result', args=(p.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})