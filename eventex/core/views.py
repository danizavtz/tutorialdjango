# coding: utf-8
from datetime import time
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from eventex.core.models import Speaker, Talk

def home(request):
    return render(request, 'index.html')

def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker,slug=slug)
    context = {'speaker': speaker}
    return render(request, 'core/speaker_detail.html', context)

def talk_list(request):
    from django.http import HttpResponse
    return HttpResponse()

def talk_list(request):
    context = { 'morning_talks':Talk.objects.at_morning(),
                'afternoon_talks':Talk.objects.at_afternoon(),
    }
    return render(request,'core/talk_list.html', context)

def talk_detail(request, pk):
    talk = get_object_or_404(Talk, pk=pk)
    context = {
        'talk': talk,        
    }
    return render(request, 'core/talk_detail.html', context)
