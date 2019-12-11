from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, './HTML/index.html')


def analyze(request):
    function_call = request.POST.get('ana-func', 'None')
    text = request.POST.get('text-area')
    new_text = ''
    purp = ''
    if function_call == 'remv-punc':
        new_text = remove_punc(text)
        purp = 'Remove Punctuations'
    elif function_call == 'remv-space':
        new_text = remove_space(text)
        purp = 'Remove Spaces'
    elif function_call == 'cap-first':
        new_text = cap_first(text)
        purp = 'Capitalize First'
    elif function_call == 'cap-all':
        new_text = cap_all(text)
        purp = 'Capitalize All'
    else:
        new_text = 'No function provided'
        purp = 'No Function'

    param = {
        'purpose': purp,
        'the_text': new_text
    }

    return render(request, './HTML/analyze.html', param)

def remove_punc(the_text):
    punctuation = ['.', ',', '!', '?', ':', ';', '\'', '-', '_', '{', '}', '[', ']']
    new = [char for char in the_text if char not in punctuation]
    new = ''.join(new)
    return new

def remove_space(the_text):
    new = [char for char in the_text if char is not ' ']
    new = ''.join(new)
    return new

def cap_first(the_text):
    new = the_text.title()
    return new

def cap_all(the_text):
    new = ''.join([char.upper() for char in the_text])
    return new