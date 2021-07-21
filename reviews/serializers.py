from rest_framework import serializers

from .models import Comment, Review


class ReviewSerializers(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        exclude = ('title',)
        model = Review

    def validate(self, data):
        user = self.context['request'].user
        title_id = self.context['view'].kwargs.get('title_id')
        method = self.context['request'].method

        if (Review.objects.filter(title=title_id, author=user)
                and method == 'POST'):
            raise serializers.ValidationError(
                'Отзыв на это произведение текущим пользователем уже написан.'
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        exclude = ('review',)
        model = Comment
