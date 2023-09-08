from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main/index.html')


@login_required(login_url='/auth/login')
def sshh(request):
    return HttpResponse("This is authenticated view !")