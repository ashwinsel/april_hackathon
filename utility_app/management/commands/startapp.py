from django.core.management.commands.startapp import Command as StartAppCommand


class Command(StartAppCommand):
    help = "Extends 'startapp' to use a custom template and replace placeholders."

    def handle(self, **options):
        if not options.get('template'):
            options['template'] = 'app_name'
        super().handle(**options)
