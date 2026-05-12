from django.shortcuts import render

from .models import Payment


def payment_list(request):
    payments = Payment.objects.select_related('appointment__patient', 'appointment__doctor', 'appointment__service')
    return render(request, 'payment_list.html', {
        'payments': payments,
    })