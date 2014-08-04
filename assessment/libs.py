__author__ = 'anithrao'
######### libs.py ####################################
# This gives you the extra functionality you'll need
######################################################
from django.contrib.formtools.wizard import FormWizard

class FormWizardSnip(FormWizard):
    def __init__(self, context):
        # Override the extra context
        self.extra_context = context

        # Call the original init
        super(FormWizardSnip, self).__init__(self._forms)

    def __call__(self, request):
        return super(FormWizardSnip, self).__call__(request)

def render_to_wizard(f, request, context):
    c = f(context=context)
    return c(request)
