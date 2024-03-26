from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Url
import uuid
from rest_framework import viewsets, permissions, status
from .serializers import UrlSerializer  
from rest_framework.response import Response


def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        if link:
            uid = str(uuid.uuid4())[:5]
            new_url = Url.objects.create(link=link, uuid=uid)  
            return HttpResponse({'uuid': uid}, content_type='application/json')
        else:
            return HttpResponse({'error': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
    else:
        return HttpResponse({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED, content_type='application/json')

def go(request, pk):
    url_details = get_object_or_404(Url, uuid=pk)
    return redirect('https://' + url_details.link)


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)