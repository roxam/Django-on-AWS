from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse

def test(request):
    return render_to_response('test.html', {}, 
        context_instance=RequestContext(request))
