from django import forms
from django.forms import ModelForm
from .models import Proyecto, Tarea, Empleado


class DateInput(forms.DateInput):
    input_type = 'date'


class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': DateInput(attrs={'class': 'form-control'}),
            'fecha_fin': DateInput(attrs={'class': 'form-control'}),
            'presupuesto': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'email_cliente': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono_cliente': forms.NumberInput(attrs={'class': 'form-control'}),
            'tarea': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
        }


class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': DateInput(),
            'fecha_fin': DateInput(),
            # responsable
            # nivel_prioridad
            'notas': forms.TextInput(attrs={'class': 'form-control'}),
            # estado_tarea
        }


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
        }
