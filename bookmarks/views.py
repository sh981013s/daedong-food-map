"""bookmarks views"""
from config.views import BaseView
from django.db.models import Q, query
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Bookmark
from .permissions import IsBookmarkEditableOrDestroyable
from .serializers import BookmarkSerializer


class BookmarkListView(BaseView, ListAPIView):
    """# BookmarkListView
    - 현재 유저가 북마크(create) 목록(place)이 반환된다.
    """
    queryset = Bookmark.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BookmarkSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.current_user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BookmarkRetrieveView(BaseView, RetrieveAPIView):
    """# BookmarkRetrieveView
    - Place 객체를 북마크한 유저를 return 한다.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = BookmarkSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.current_user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class BookmarkCreateView(BaseView, CreateAPIView):
    """# BookmarkCreateView
    - 북마크를 생성한다.
    """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        place_id = self.request.POST["place_id"]

        if Bookmark.objects.filter(
            Q(place = place_id) &
            Q(user = self.current_user)):
            return JsonResponse({'alreadyExists': 'True'})
        else:
            serializer.save(user=self.current_user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookmarkDestroyView(BaseView, DestroyAPIView):
    """# BookmarkDestroyView
    - 북마크를 해제한다.
    """

    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated, IsBookmarkEditableOrDestroyable]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.current_user)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.place.bookmark_count -= 1
        obj.place.save()
        return self.destroy(request, *args, **kwargs)
