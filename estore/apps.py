from django.apps import AppConfig


class EstoreConfig(AppConfig):
    name = 'estore'
<<<<<<< HEAD

    def ready(self):
        from . import signals
=======
    
    def ready(self):
        from . import signals
>>>>>>> 38e9ecd4eaae03ef4084980fa893f1aa5e42b94e
