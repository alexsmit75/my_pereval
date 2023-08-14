from django.urls import path
from .views import SubmitDataView

urlpatterns = [
    path('submit-data/', SubmitDataView.as_view(), name='submit-data'),
]