from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect



class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        if not  self.request.user.is_authenticated :
            return HttpResponseRedirect("login")
        if self.request.user.is_superuser:
            return True