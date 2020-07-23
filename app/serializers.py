from django.utils.safestring import mark_safe
from markdownx.utils import markdownify
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    main_text = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_main_text(self, obj):
        return obj.convert_markdown_to_html()
