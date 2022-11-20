from django import template
import re

register = template.Library()

@register.filter()
def censor(text):
    if isinstance(text, str):
        wordstocensor = ['fool', 'death', 'suffer']
        text = re.split('(\W+)', text)
        for i, j in enumerate(text):
            for k in wordstocensor:
                if k in j.lower():
                    text[i] = text[i][0] + '*'*(len(text[i]) - 1)
        return ''.join(text)
    else:
        raise Exception("This filter is applicable only to the <class 'str'>")