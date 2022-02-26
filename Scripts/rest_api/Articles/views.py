from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .serializers import ArticleModelSerializer, UserSerializer
from .models import Article
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

# Create your APIviews here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


def index(request):

    return HttpResponse('it works')

@csrf_exempt
def articles(request):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        # return HttpResponse(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        # return HttpResponse(data)
        serializer = ArticleModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def articles_apiview(request):
    # permission_classes = [IsAuthenticated]
    authentication_classes = TokenAuthentication
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def articles_detail(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ArticleModelSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleModelSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()

        return HttpResponse(status=204)



@api_view(['PUT','DELETE','GET'])
def articles_detail_apiview(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ArticleModelSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleModelSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()

        return HttpResponse(status=204)
    

class ArticleViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class= ArticleModelSerializer


# Generic View Set
class ArticleGenericViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin

                            ):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer



# Model Vew set
class ArticleModelViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

#
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserViewSets(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return  Response(serializer.data)
#
#     def post(self,request,format=None):
#         serializer = UserSerializer(data=request.data)
#
#         if serializer.is_valid():
#             Token.objects.create(user=serializer)
#             serializer.save()
#
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






