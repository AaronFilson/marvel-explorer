from .serializers import ComicSerializer
from rest_framework import permissions
from m_profile.permissions import IsObjectOwner
from rest_framework import (
    authentication,
    generics,
    )
from .models import Comic


class UserComicsCreate(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsObjectOwner,)

    queryset = Comic.objects.all()
    serializer_class = ComicSerializer


class UserComicsUpdate(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsObjectOwner,)

    queryset = Comic.objects.all()
    serializer_class = ComicSerializer
