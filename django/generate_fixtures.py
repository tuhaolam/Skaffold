from django.core.management.base import BaseCommand, CommandError
from {{{ project }}}.{{{ app_name }}} import model_factories

MAX_RECORDS = 10


class Command(BaseCommand):
    help = 'Adds all fixture data.'

    def handle(self, *args, **options):
        for _ in xrange(MAX_RECORDS):
        {%% for model_name in all_models %%}
            {%% set model_name = model_name|capitalize %%}
            model_factories.{{{ model_name }}}Factory()
        {%% endfor %%}
