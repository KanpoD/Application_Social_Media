from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
   # created_by = UserSerializer(read_only=True)
  #  attachments = PostAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'body', 'created_at', 'created_by', 'attachments')
