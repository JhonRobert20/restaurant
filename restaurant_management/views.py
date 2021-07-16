from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse


def index(request):
    return redirect('/admin/')


