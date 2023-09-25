from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views import View
from .models import Forms
from .forms import FormsForm


class BaseView(LoginRequiredMixin, View):
    def get(self, request):
        forms = Forms.objects.order_by('-date')
        return render(request, 'main/main.html', {'forms': forms})


class AboutView(LoginRequiredMixin, View):
    def get(self, request):
        form = FormsForm()
        data = {
            'form': form,
        }
        return render(request, 'main/form.html', data)

    def post(self, request):
        if request.method == 'POST':
            form = FormsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/main')


class JAnketsView(LoginRequiredMixin, View):
    def get(self, request):
        offset = int(request.GET.get('offset', 20))
        data = Forms.objects.all().order_by('id')[offset:offset+5].values(
            'id', 'title', 'name', 'age', 'comment', 'date')
        for item in data:
            item['date'] = item['date'].strftime('%b. %d, %Y, %I:%M %p')
        return JsonResponse(list(data), safe=False)


class AnketsView(LoginRequiredMixin, View):
    def get(selfs, request):
        data = Forms.objects.all().order_by('id')[:20]
        return render(request, 'main/ankets.html', {'data': data})