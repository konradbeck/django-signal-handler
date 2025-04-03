import logging
from typing import Any

from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.db.models.signals import pre_save

logger = logging.getLogger(__name__)


class SignalHandler:
    """Base class for handling Django model signals."""

    def run(self, sender: type, instance: Any, **kwargs: Any) -> None:
        """
        Determines the signal type and calls the appropriate handler method.

        Args:
            sender: The model class.
            instance: The model instance.
            **kwargs: Additional keyword arguments from the signal.
        """
        signal_obj = kwargs.get("signal")

        if signal_obj == pre_save:
            if instance.pk is None:
                self.pre_save_new(instance, **kwargs)
            else:
                self.pre_save_update(instance, **kwargs)
        elif signal_obj == post_save:
            if kwargs.get("created", False):
                self.post_save_new(instance, **kwargs)
            else:
                self.post_save_update(instance, **kwargs)
        elif signal_obj == pre_delete:
            self.pre_delete(instance, **kwargs)
        elif signal_obj == post_delete:
            self.post_delete(instance, **kwargs)
        else:
            logger.warning("Unknown or missing signal in kwargs: %s", signal_obj)

    def pre_save_new(self, instance: Any, **kwargs: Any) -> None:
        """Handler for pre_save signals when a new instance is being created."""

    def post_save_new(self, instance: Any, **kwargs: Any) -> None:
        """Handler for post_save signals when a new instance is created."""

    def pre_save_update(self, instance: Any, **kwargs: Any) -> None:
        """Handler for pre_save signals when an existing instance is being updated."""

    def post_save_update(self, instance: Any, **kwargs: Any) -> None:
        """Handler for post_save signals when an existing instance is updated."""

    def pre_delete(self, instance: Any, **kwargs: Any) -> None:
        """Handler for pre_delete signals."""

    def post_delete(self, instance: Any, **kwargs: Any) -> None:
        """Handler for post_delete signals."""
