# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {'latest_question_list': [1, 2, 3]}
    return render(request, 'fangdong/index.html', context)
