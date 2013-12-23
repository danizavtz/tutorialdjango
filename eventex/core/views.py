# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from eventex.core.models import Speaker

def home(request):
    return render(request, 'index.html')

def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker,slug=slug)
    context = {'speaker': speaker}
    return render(request, 'core/speaker_detail.html', context)
