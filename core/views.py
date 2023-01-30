from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import FrameworkModel
from .serializers import FrameworkSerializer


class FrameworkListView(ListAPIView):
    """View for a list of all objects"""
    queryset = FrameworkModel.objects.all()
    serializer_class = FrameworkSerializer


class FrameworkDetailView(ListAPIView):
    """View for framework by language"""
    serializer_class = FrameworkSerializer

    def get_queryset(self):
        language = self.kwargs['language']
        return FrameworkModel.objects.filter(language=language)
