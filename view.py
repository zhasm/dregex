from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from option import Option
from textarea import TextArea

reoptions = [
            ('s', 'dotall', 'Dot Match All'),
            ('i', 'ignorecase', 'Case Insensitive'),
            ('m', 'multiline', '^$ at line breaks'),
            ('x','verbose','Free-Spacing'),
            ('u', 'unicode', 'Unicode')
        ]

funcs = [
        '',
    'Import regex library',
    'If/else branch whether the regex matches (part of) a string'
    ]

langs= ['python',]

ops=Option()
text=TextArea()

def index(request):
    global ops, text
    ops.__init__()
    text.__init__()
    t = get_template("index.html")
    html = t.render(Context({"reoptions":reoptions, "langs":langs, "funcs":funcs}))
    return HttpResponse(html)
    
def option(request, name, value):
    global ops
    if name:
        ops.set(name, value)
    
def textarea(request):
    global text
    name = request.POST.get('name', '')
    value = request.POST.get('value', '')
    if name:
        text.set(name, value)
    text.do(ops)
    return HttpResponse(ops.get_repr()+text.get()+text.result)