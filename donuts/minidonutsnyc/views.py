from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views import generic


def index(request):
    template = loader.get_template('minidonutsnyc/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
#    return render(request, 'minidonutsnyc/index.html', {})


#class IndexView(generic.DetailView):
#    template_name = 'minidonutsnyc/index.html'
