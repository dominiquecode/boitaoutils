from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):

    message_ok = "L'admin a bien été créé. N'oubliez pas de modifier le mot de passe par défaut!"
    message_no = "L'admin existe déjà!"

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').count():
            try:
                user = User.objects.create_superuser('admin', 'admin@tradom.ca', 'pass')

            except:
                raise CommandError("Problème de création de l'admin")

            user.save()
            self.stdout.write(self.style.SUCCESS(self.message_ok))
        else:
            self.stdout.write(self.style.ERROR(self.message_no))
