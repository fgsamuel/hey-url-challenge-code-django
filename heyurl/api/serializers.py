from rest_framework import serializers


class UrlAttributes(serializers.Serializer):
    created_at = serializers.DateTimeField()
    original_url = serializers.URLField()
    url = serializers.SerializerMethodField()
    clicks = serializers.IntegerField()

    def get_url(self, obj):
        return obj.short_url


class UrlSerializer(serializers.Serializer):
    type = serializers.SerializerMethodField()
    id = serializers.IntegerField()
    attributes = serializers.SerializerMethodField()

    def get_type(self, obj):
        return 'urls'

    def get_attributes(self, obj):
        return UrlAttributes(obj).data
