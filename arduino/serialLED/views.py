from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
import serial

from datetime import datetime


class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        if request.method == 'POST':
            if 'LED' in request.POST:
                ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
                ser.write(1)
                ser.close()
        return render(request, self.template_name)


def output(request):
    while True:
        ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
        a = ""
        for x in range(5):
            out = ser.read()
            out2 = out.strip().decode('utf-8')
            a = a + out2
        if float(a) < 500:
            context = {'result': a}
            return render(request, 'index3.html', context)
        else:
            return render(request, 'index5.html')
            break


def top(request):
    return render(request, "index4.html")




def exercise(request):
    now = datetime.now()
    context = {
        'text': "It's test",
        'time': now,
    }
    return render(request, 'index2.html', context)
