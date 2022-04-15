from django.shortcuts import redirect, render
from .models import Resume
from .forms import ResumeForm
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'uploaderapp/home.html', {'form':form, 'candidates':candidates})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect("home")


class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'uploaderapp/candidate.html', {'candidate':candidate})