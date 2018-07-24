from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db.models import Count
# from django.contrib.messages import get_messages
from .models import *
import bcrypt

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    # context = {

    # }
    return render(request,'Awareness/index.html')