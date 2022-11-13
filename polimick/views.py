from django.http import HttpResponseRedirect
def view_404(request, exception=None):
    return HttpResponseRedirect("/")