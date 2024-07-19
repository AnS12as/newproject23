from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
