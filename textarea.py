import re
from option import Option

color_index=1
ERROR_HTML="""<div class='ui-state-error ui-corner-all'><p><span class="ui-icon ui-icon-alert" style="float: left; margin-right: 0.3em;"></span> 
<strong>Alert:</strong> %s</p></div>"""

def generate_color():
    global color_index
    color_index *= -1
    if color_index == -1:
        return "<hl>%s</hl>"
    else:
        return "<lh>%s</hl>"
    
    
class TextArea:
    ''' receive textarea updates, and process them accordingly
    use Unicode regex by default
    POST-> regex, test, replace
    Return-> result
    '''
    
    
    def __init__(self):
        self.regex=ur""
        self.text=ur""
        self.replace=ur""
        self.result=ur""

    def set(self, name, value):
        #result can never be set by the front-end, only by back-end
        if name in ("regex", "text", "replace"):
            self.__dict__[name]=value
            
    def get(self):
        return """<b>Regex</b>: %s<br>
<b>Replace</b>: %s<br>
<b>Text</b>: %s<br>""" % (self.regex, self.replace, self.text) 
    
        
    def do(self, option):
        '''the core engine of the program'''
        #compile the regex, and replace the matched part with hilighted format
        if not self.text:
            self.result=""
            return
        if not self.regex:
            self.result=""
            return
        regex=re.compile(self.regex, option.get_flags())
        def re_wrapper(reobj):
            return generate_color() % reobj.group(0)
        
        
        #match action
        if option.action==0:
            try:
                count=len(regex.findall(self.text))
                if count:
                    self.result= regex.sub(re_wrapper, self.text)
                    self.result=( "<b>Match Details</b>: %d matches found:<br/><pre>" % count ) \
                        + (self.result) +"</pre>"

                else:
                    self.result="No match."
            except:
                self.result="Match Error."
        #replace action
        elif option.action==1:
            try:
                self.result=regex.sub(self.replace, self.text)
                self.result=re.sub(r"<(?!hl|lh)", "&lt;", self.result)
                self.result=re.sub(r"(?<!hl|lh)>", "&gt;", self.result)
                self.result="<b>Replaced result</b>: "+ self.result
            except:
                self.result=ERROR_HTML % "Replace Error"
        #split
        elif option.action==2:
            try:
                x=regex.split(self.text)
                x=[i for i in x if i]
                self.result="<ul><li>%s</li></ul>" % ("</li><li>".join(x))
            except:
                self.result="split error"
        else:
            self.result=str(option.action)
        
