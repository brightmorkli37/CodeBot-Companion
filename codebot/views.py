from django.shortcuts import render


def homepage(request):
    template_name = 'codebot/homepage.html'
    context = {}
    return render(request, template_name, context)
