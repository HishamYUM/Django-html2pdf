
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import dataModel
from django.views import View
# Create your views here.
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    pdf_status = pisa.CreatePDF(html, dest=response)

    if pdf_status.err:
        return HttpResponse('Some errors were encountered <pre>' + html + '</pre>')

    return response

def get(request, *args, **kwargs):
    template_name = 'base/main.html'
    records = dataModel.objects.all().order_by("s_no")
    context = {'records':records}
    return render_to_pdf(template_name, context)

def home(request):
    records = dataModel.objects.all().order_by("s_no")
    context = {'records':records}
    return render(request, "base/main.html", context)