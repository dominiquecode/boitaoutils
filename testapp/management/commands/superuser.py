from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').count():
            try:
                user = User.objects.create_superuser('admin', 'admin@tradom.ca', 'pass')

            except:
                raise CommandError("Problème de création de l'admin")

            user.save()
            self.stdout.write(self.style.SUCCESS("L'admin est créé"))
        else:
            self.stdout.write(self.style.ERROR("L'admin existe déjà!"))
