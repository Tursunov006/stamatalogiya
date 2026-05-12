from django.shortcuts import render

from .models import Doctor


def doctor_list(request):
    doctors = Doctor.objects.filter(active=True)
    return render(request, 'doctor_list.html', {
        'doctors': doctors,
    })