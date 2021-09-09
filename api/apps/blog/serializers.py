from rest_framework import serializers
from apps.blog.models import Blog
from apps.accounts.serializers import UserSerializer



class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.pk")
    class Meta:
        model = Blog
        fields = (
            "pk",
            "author",
            "title",
            "slug",
            "article",
            "views",
            "share",
            "pub_date"
        )

        extra_kwargs = {
            "slug": {"read_only": True}
        }

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp["author"] = UserSerializer(instance=instance.author).data
        return resp

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)
