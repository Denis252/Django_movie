from django import template
from contact.forms import ContactForm

register = template.Library()

@register.inclusion_tag("contact/tags/form.html")
def contact_forms():
    return {"contact_form": ContactForm()}