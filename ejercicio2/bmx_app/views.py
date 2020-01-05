import decimal

import requests
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView

from bmx_app.forms import DateRangeForm


class DateRangeView(FormView):
    template_name = 'bmx_app/date_range.html'
    form_class = DateRangeForm

    def form_valid(self, form):
        self.serie = form.cleaned_data['serie']
        self.start_date = form.cleaned_data['start_date']
        self.end_date = form.cleaned_data['end_date']
        return super().form_valid(form)

    def get_success_url(self):
        print('get_success_url')
        return reverse('data', kwargs={'serie': self.serie,
                                       'fechaInicial': self.start_date,
                                       'fechaFinal': self.end_date})


class DataView(View):
    template_name = 'bmx_app/data.html'

    def get(self, request, *args, **kwargs):
        serie = kwargs.get('serie')
        fechaInicial = kwargs.get('fechaInicial')
        fechaFinal = kwargs.get('fechaFinal')
        url = settings.BMXAPI['data_range_url'].format(
            serie=serie,
            fechaInicial=fechaInicial,
            fechaFinal=fechaFinal
        )
        try:
            resp = requests.get(url, headers={
                'Bmx-Token': settings.BMXTOKEN,
                'Accept': 'application/json'
            })
            resp.raise_for_status()
        except (requests.RequestException,
                requests.ConnectionError,
                requests.HTTPError,
                requests.Timeout,
                ) as e:
            return render(requests, 'error.html', {'message': str(e)})
        data = resp.json()
        for serie in data['bmx']['series']:
            if not serie.get('datos'):
                serie['datos'] = None
            else:
                values = []
                labels = []
                for dato in serie['datos']:
                    dato['value'] = decimal.Decimal(dato['dato'])
                    values.append(dato['value'])
                    labels.append(dato['fecha'])
                serie['avg'] = sum(values)/len(values)
                serie['min'] = min(values)
                serie['max'] = max(values)
                serie['max_index'] = [i for i, j in enumerate(
                    values) if j == serie['max']]
                serie['data'] = list(map(float, values))
                serie['labels'] = labels
                serie['title'] = serie['titulo'][:40].strip()
        return render(request, self.template_name,
                      {'data': data,
                       'fechaInicial': fechaInicial,
                       'fechaFinal': fechaFinal})
