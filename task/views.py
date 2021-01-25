from django.contrib.auth import get_user_model, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import LoginForm, Save_Schemas_Form
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from .models import DataModel
from .serializers import Data_Serializers
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.mixins import ListModelMixin
import csv

Users = get_user_model()


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('all/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def all_shem(request):
    courses = DataModel.objects.all()
    return render(request, 'all_shem.html', {'courses': courses})


def save_schemas(request):
    if request.method == 'POST':
        form = Save_Schemas_Form(data=request.POST)
        if form.is_valid():
            ful_name = form.cleaned_data.get('ful_name')
            job = form.cleaned_data.get('job')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            description = form.cleaned_data.get('description')
            date = form.cleaned_data.get('date')

            purchase = DataModel(ful_name=ful_name, job=job, email=email, phone=phone, description=description,
                                 date=date)
            purchase.save()
            return redirect('http://127.0.0.1:8000/all')
    else:
        form = Save_Schemas_Form()
    return render(request, 'save_schemas.html', {'form': form})


def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Ful Name', 'Job', 'Email', 'Phone', 'Description', 'Date'])

    for member in DataModel.objects.all().values_list('ful_name', 'job', 'email', 'phone', 'description', 'date'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="schemas.csv"'

    return response


class CreateVieAll(RetrieveUpdateDestroyAPIView):
    serializer_class = Data_Serializers
    queryset = DataModel.objects.all()

