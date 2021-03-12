from django.views.generic import TemplateView, View, ListView
from resume.models import Resume
from django.shortcuts import redirect
from django.http import HttpResponseForbidden


class ResumeListView(TemplateView):
    template_name = 'first_page/resumes.html'

    def get_context_data(self, **kwargs):
        context = super(ResumeListView, self).get_context_data(**kwargs)
        # here's the difference:
        context['resumes'] = Resume.objects.all()
        # print(context)
        return context


class AddResumeView(View):
    def post(self, request):
        user = request.user
        description = request.POST.get('description')
        Resume.objects.create(author=user, description=description)
        return redirect('/')
