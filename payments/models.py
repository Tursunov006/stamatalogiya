from django.db import models
from appointments.models import Appointment


PAYMENT_STATUS = [
    ('pending', 'Kutilmoqda'),
    ('paid', 'To‘langan'),
    ('cancelled', 'Bekor qilingan'),
]


class Payment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=12, choices=PAYMENT_STATUS, default='pending')
    transaction_id = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.appointment} - {self.get_status_display()}"

    @property
    def badge_class(self):
        return {
            'pending': 'secondary',
            'paid': 'success',
            'cancelled': 'danger',
        }.get(self.status, 'secondary')
