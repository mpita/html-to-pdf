from django.views.generic import View
from django.utils import timezone
from .models import *
from .render import Render


class Pdf(View):

    def get(self, request):
        sales = Sales.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'sales': sales,
            'request': request
        }
        return Render.render('pdf.html', params)
