from rest_framework import permissions, viewsets
from rest_framework.generics import get_object_or_404

from categories.models import Title

from .models import Review
from .permissions import IsAuthorModerAdmin
from .serializers import CommentSerializer, ReviewSerializers


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorModerAdmin]

    def perform_create(self, serializer):
        review_id = self.kwargs['review_id']
        review = get_object_or_404(Review, pk=review_id)
        serializer.save(author=self.request.user, review_id=review.id)

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        title_id = self.kwargs['title_id']
        review = get_object_or_404(Review, title__id=title_id, pk=review_id)
        queryset = review.comments.all()
        return queryset


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorModerAdmin]

    def perform_create(self, serializer):
        title_id = self.kwargs['title_id']
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title_id = self.kwargs['title_id']
        title = get_object_or_404(Title, pk=title_id)
        queryset = title.reviews.all()
        return queryset
