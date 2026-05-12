from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Appointment, TIME_SLOT_CHOICES
from patients.models import Patient
from doctors.models import Doctor
from services.models import Service


class AppointmentForm(forms.ModelForm):
    first_name = forms.CharField(label=_('Ism'), max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ismingiz'}))
    last_name = forms.CharField(label=_('Familiya'), max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Familiyangiz'}))
    phone = forms.CharField(label=_('Telefon'), max_length=20, widget=forms.TextInput(attrs={'placeholder': '+998991234567'}))
    email = forms.EmailField(label=_('E-pochta'), required=False, widget=forms.EmailInput(attrs={'placeholder': 'name@example.com'}))
    birth_date = forms.DateField(
        label=_('Tug‘ilgan sana'),
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Appointment
        fields = ['doctor', 'service', 'appointment_date', 'time_slot', 'notes']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time_slot': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Qo‘shimcha ma’lumot...'}),
        }
        labels = {
            'doctor': _('Stomatolog'),
            'service': _('Xizmat'),
            'appointment_date': _('Sana'),
            'time_slot': _('Vaqt'),
            'notes': _('Izoh'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.filter(active=True)
        self.fields['doctor'].widget.attrs.update({'class': 'form-select'})
        self.fields['service'].queryset = Service.objects.filter(active=True)
        self.fields['service'].widget.attrs.update({'class': 'form-select'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['birth_date'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get('doctor')
        appointment_date = cleaned_data.get('appointment_date')
        time_slot = cleaned_data.get('time_slot')

        if doctor and appointment_date and time_slot:
            # Check if slot is already booked
            existing = Appointment.objects.filter(
                doctor=doctor,
                appointment_date=appointment_date,
                time_slot=time_slot,
                status__in=['pending', 'confirmed']
            ).exclude(pk=self.instance.pk if self.instance else None)

            if existing.exists():
                raise forms.ValidationError(
                    f"Ushbu vaqt ({time_slot}) allaqachon band. Boshqa vaqtni tanlang."
                )

        return cleaned_data
