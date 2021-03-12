from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from vacancy.models import Vacancy
from django.http import HttpResponseForbidden


class VacancyListView(TemplateView):
    template_name = 'first_page/vacancies.html'

    def get_context_data(self, **kwargs):
        context = super(VacancyListView, self).get_context_data(**kwargs)
        # here's the difference:
        context['vacancies'] = Vacancy.objects.all()
        # print(context)
        return context


class AddVacancyView(View):
    def post(self, request):
        user = request.user
        if user.is_staff:
            description = request.POST.get('description')
            Vacancy.objects.create(author=user, description=description)
            return redirect('/')
        else:
            return HttpResponseForbidden()
