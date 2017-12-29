"""Views for mercadopublico_api"""
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
import datetime
from .models import CompraPublica, APIList, APIItem

class IndexView(generic.ListView):
    template_name = 'mercadopublico_api/index.html'

    def get_queryset(self):
        """Returnd the last five published CompraPublica."""
        return APIList.objects.all()[:5]

def index(request):
    return render(request, 'mercadopublico_api/index.html', {'total': APIList.objects.count()})

def detail(request, code):
    cp = CompraPublica.create(code)
    return render(request, 'mercadopublico_api/detail.html', {'cp': cp})

def list(request,
         year=timezone.now().year,
         month=timezone.now().month,
         day=timezone.now().day):
    apilist, new = APIList.create(is_licitacion=False,
                                  date=datetime.date(year,month,day))
    return render(request, 'mercadopublico_api/list.html', {'list': apilist})

#class IndexView(generic.ListView):
#    template_name = 'mercadopulbico_api/index.html'
#    context_object_name = 'latest_question_list'
#
#    def get_queryset(self):
#        """
#        Return the last five published questions (not including those
#        set to be published in the future).
#        """
#        return Question.objects.filter(
#            pub_date__lte=timezone.now()
#        ).order_by('-pub_date')[:5]
#
#class DetailView(generic.DetailView):
#    model = Question
#    template_name = 'polls/detail.html'
#
#    def get_queryset(self):
#        """
#        Excludes any questions that aren't published yet.
#        """
#        return Question.objects.filter(pub_date__lte=timezone.now())
