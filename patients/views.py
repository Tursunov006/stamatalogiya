from django.shortcuts import render

from .models import Patient


def patient_list(request):
    patients = Patient.objects.order_by('last_name', 'first_name')
    return render(request, 'patient_list.html', {
        'patients': patients,
    })