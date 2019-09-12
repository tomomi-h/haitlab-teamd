from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
import serial


class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        if request.method == 'POST':
            if 'LED' in request.POST:
                ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
                ser.write(1)
                ser.close()
        return render(request, self.template_name)

class IndexTemplateView2(TemplateView):
    template_name = "index2.html"

    def check(self):
        ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
        while True:
            a = ""
            for x in range(5):
                out = ser.read()
                out2 = out.strip().decode('utf-8')
                a = a + out2
            return a

    def output(request):
        context = {'result' : check(),}
        return render(request, 'index2.html', context)

