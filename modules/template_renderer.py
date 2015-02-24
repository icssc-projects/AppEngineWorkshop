import jinja2
import os

_JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/../templates'),
    extensions=['jinja2.ext.autoescape', 'jinja2.ext.loopcontrols'],
    autoescape=True)

print(os.path.dirname(__file__))

def render(template, values):
    return _JINJA_ENVIRONMENT.get_template(template).render(values)
