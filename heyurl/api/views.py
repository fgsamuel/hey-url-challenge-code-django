from rest_framework.generics import ListAPIView

from heyurl.api.serializers import UrlSerializer
from heyurl.models import Url


class UrlListView(ListAPIView):
    queryset = Url.objects.all().order_by('-created_at')[:10]
    serializer_class = UrlSerializer
