from django import forms
from django.forms.widgets import SelectDateWidget
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

now = timezone.now()
start = now - timedelta(days=7)


class DateRangeForm(forms.Form):
    choices = ((settings.BMXAPI['udis_serie'], 'Valor de UDIS'),
               (settings.BMXAPI['dolar_serie'], 'Tipo de cambio Pesos por dólar E.U.A.'),
               (settings.BMXAPI['tiie28_serie'], 'TIIE a 28 días'),
               (settings.BMXAPI['tiie91_serie'], ' TIIE a 91 días'),
               (settings.BMXAPI['tiie182_serie'], 'TIIE a 182 días'))
    serie = forms.ChoiceField(choices=choices)
    start_date = forms.DateField(label='fecha inicial',
                                 initial=start.date(),
                                 required=True,
                                 widget=SelectDateWidget(
                                     years=range(1991, now.year+1)))
    end_date = forms.DateField(label='fecha final',
                               initial=now.date(),
                               widget=SelectDateWidget(
                                   years=range(1991, now.year+1)))

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if not start_date or end_date:
            return
        if start_date > end_date:
            raise forms.ValidationError(
                "fecha inicio debe ser anterior o igual a fecha final"
            )
        return cleaned_data
