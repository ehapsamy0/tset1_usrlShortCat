
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from .models import KirrURL

# Create your views here.




def kirr_redirect_view(request,shortcode=None,*args,**kwargs):
    # obj = KirrURL.objects.get(shortcode=shortcode)

    obj = get_object_or_404(KirrURL,shortcode=shortcode)
    obj_url = obj.url
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()

    #
    # obj_url = None
    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() or qs.count()==1:
    #     obj = qs.first()
    #     obj_url = obj.url
    return HttpResponseRedirect(obj.url)


class KirrCBView(View):

    def get(self,request,shortcode=None,*args,**kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        obj_url = obj.url
        return HttpResponseRedirect(obj.url)
