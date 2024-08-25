"""
Django cmd to wait db to be ready
"""

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as PsycopgError
import time


class Command(BaseCommand):
    """Cmd to wait for db"""

    def handle(self, *args, **options):
        """Entry point for cmd"""
        self.stdout.write("waiting for db...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (OperationalError, PsycopgError):
                self.stdout.write("Database not ready waiting 1s...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is ready!"))
