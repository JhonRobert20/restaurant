from django.apps import AppConfig


class RestaurantManagementConfig(AppConfig):
    name = 'restaurant_management'

    def ready(self):
        print(f"{self.name} ({self.__class__}): to be ready soon")
        # Do things on ready process... ie: connecting signals
        print(f"{self.name} ({self.__class__}): Ready")
