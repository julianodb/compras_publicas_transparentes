from django.shortcuts import render
from django.views import generic
from .models import CompraPublica

class IndexView(generic.ListView):
    template_name = 'mercadopublico_api/index.html'
#    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published CompraPublica."""
        return CompraPublica.get_last_five()

def detail(request,code):
    cp = CompraPublica(code)
    return render(request, 'mercadopublico_api/detail.html',{'cp': cp})

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

