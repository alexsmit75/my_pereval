from .models import PerevalAdded

class DataManager:
    def add_pereval(self, data):
        pereval = PerevalAdded.objects.create(
            beautyTitle=data['beauty_title'],
            title=data['title'],
            other_titles=data['other_titles'],
            connect=data['connect'],
            add_time=data['add_time'],
            status='new'
        )

        return pereval.id


data_manager = DataManager()