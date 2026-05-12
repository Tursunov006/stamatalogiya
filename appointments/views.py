from django.shortcuts import render, redirect

from .forms import AppointmentForm
from .models import Appointment
from doctors.models import Doctor
from services.models import Service
from patients.models import Patient


def home(request):
    context = {
        'service_count': Service.objects.filter(active=True).count(),
        'doctor_count': Doctor.objects.filter(active=True).count(),
        'appointment_count': Appointment.objects.count(),
        'patient_count': Patient.objects.count(),
        'recent_appointments': Appointment.objects.select_related('patient', 'doctor', 'service').order_by('-created_at')[:5],
    }
    return render(request, 'index.html', context)


def appointment_list(request):
    appointments = Appointment.objects.select_related('patient', 'doctor', 'service').order_by('appointment_date', 'time_slot')
    return render(request, 'appointment_list.html', {
        'appointments': appointments,
    })


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()

    return render(request, 'booking.html', {
        'form': form,
    })