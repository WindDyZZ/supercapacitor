from ui.models import Data

def run():
    # Delete all existing data
    Data.objects.all().delete()