"""Update all dashboards django admin command."""
from typing import Any

from api.dashboards import update_all_dashboards
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Update all dashboards command class."""

    help = "Update all the grafana dashboards in the folder"

    def handle(self, *args: Any, **options: str) -> None:
        """Handle the call to update_all_dashboards command."""
        update_all_dashboards()