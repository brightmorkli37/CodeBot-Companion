from django.shortcuts import render, redirect
from django.contrib import messages
import environ
import openai

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


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

        # print(code, lang)

        if code == '':
            messages.warning(request, 'Input Code to Inspect')

        if lang == 'Select Programming Language':
            messages.warning(request, "No Programming Language selected")
            
            return redirect('homepage')
        
        # OPEN AI CONFIG
        # Key
        openai.api_key = env('OPENAI_SECRET_KEY')
        # Create OpenAI Instance
        openai.Model.list()
        #Make OpenAI Request
        try:
            response = openai.Completion.create(
                engine = 'text-davinci-003',
                prompt = f"Respond with only code. Fix this {lang} code: {code}",
                temperature = 0, 
                max_tokens = 1000,
                top_p = 1.0,
                frequency_penalty = 0.0,
                presence_penalty = 0.0,
            )
            # parse response
            response = (response["choices"][0]["text"].strip())
            return render(request, 'codebot/homepage.html', {'lang_list': lang_list, 'response': response})
        except Exception as e:
            return render(request, 'codebot/homepage.html', {'lang_list': lang_list, 'response': e})
            

    template_name = 'codebot/homepage.html'
    context = {
        'lang_list': lang_list, 'code': code,
        'lang': lang,
    }
    return render(request, template_name, context)

