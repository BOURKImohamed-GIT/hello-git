from django.http import HttpResponse

from . import translation
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.utils.translation import gettext as _
from .models import Choice, Question

class IndexView(generic.ListView):
      template_name = 'polls/index.html'
      context_object_name = 'latest_question_list'
      context = {'available_languages': ['en', 'es', 'fr']}
      def get_queryset(self):
           return Question.objects.order_by('-pub_date')[:5]
           return (context)
class DetailView(generic.DetailView):
      model = Question
      template_name = 'polls/detail.html'

def my_view(request):
     output = _("Welcome to my site.")

     return HttpResponse(output)

