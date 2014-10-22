from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from mikepolls.models import Question, Choice
from django.core.urlresolvers import reverse
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'mikepolls/index.html'
    context_object_name = 'questions'
    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    template_name ='mikepolls/detail.html'
    model = Question

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'mikepolls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('mikepolls:results', args=(p.id,)))


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'mikepolls/results.html'
    def get_queryset(self):
        return Question.objects.all()
