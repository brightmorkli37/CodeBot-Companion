from django.shortcuts import render


def homepage(request):
    lang_list = [
                    'c', 'clike', 'cpp', 'csharp', 'css', \
                    'dart', 'go', 'html', 'java', 'javascript', \
                    'julia', 'kotlin', 'markup', 'markup-templating', \
                    'matlab', 'mongodb', 'objectivec', 'perl', 'php', \
                    'plsql', 'powershell', 'python', 'r', 'ruby', 'sass', \
                    'scala', 'sql', 'swift', 'typescript' \
                ]

    code = ''
    lang = ''
    if request.method == 'POST':
        code = request.POST['code']
        lang = request.POST['lang']

    template_name = 'codebot/homepage.html'
    context = {
        'lang_list': lang_list, 'code': code,
        'lang': lang,
    }
    return render(request, template_name, context)
