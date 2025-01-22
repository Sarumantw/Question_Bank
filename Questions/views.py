from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import question
# Create your views here.
def Questions(request):
    all_questions = question.objects.all().values()
    template = loader.get_template('allquestions.html')
    context = {
        'all_questions':all_questions
        }
    return HttpResponse(template.render(context, request))
