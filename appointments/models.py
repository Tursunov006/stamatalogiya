from django.db import models

APPOINTMENT_STATUS = [
    ('pending', 'Kutilmoqda'),
    ('confirmed', 'Tasdiqlangan'),
    ('cancelled', 'Bekor qilingan'),
    ('completed', 'Bajarildi'),
]

TIME_SLOT_CHOICES = [
    ('09:00', '09:00 - 10:00'),
    ('10:00', '10:00 - 11:00'),
    ('11:00', '11:00 - 12:00'),
    ('12:00', '12:00 - 13:00'),
    ('14:00', '14:00 - 15:00'),
    ('15:00', '15:00 - 16:00'),
    ('16:00', '16:00 - 17:00'),
]


class Appointment(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    time_slot = models.CharField(max_length=20, choices=TIME_SLOT_CHOICES)
    status = models.CharField(max_length=12, choices=APPOINTMENT_STATUS, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-appointment_date', 'time_slot']

    def __str__(self):
        return f"{self.patient} - {self.doctor} ({self.appointment_date} {self.time_slot})"

    @property
    def status_badge(self):
        return {
            'pending': 'secondary',
            'confirmed': 'success',
            'cancelled': 'danger',
            'completed': 'primary',
        }.get(self.status, 'secondary')
