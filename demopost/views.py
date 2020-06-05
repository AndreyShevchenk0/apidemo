#from django.shortcuts import render
from rest_framework import generics
from demopost.serializers import CarDetailSerializer, CarsListSerializer
from demopost.models import Car
from demopost.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView


# создание
class CarCreateView(generics.CreateAPIView,):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated,)  # или IsAdminUser***********

# Просмотр конкретних записей, редактирование и удаление!

class CarDetailView(generics. RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer                # испитания
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly)
    #name = 'coment_list'
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

# JWT user/views
# @api_view(['POST'])
# @permission_classes([AllowAny, ])
# def authenticate_user(request):
#     try:
#         email = request.data['email']
#         password = request.data['password']
#
#         user = User.objects.get(email=email, password=password)
#         if user:
#             try:
#                 payload = jwt_payload_handler(user)
#                 token = jwt.encode(payload, settings.SECRET_KEY)
#                 user_details = {}
#                 user_details['name'] = "%s %s" % (
#                     user.first_name, user.last_name)
#                 user_details['token'] = token
#                 user_logged_in.send(sender=user.__class__,
#                                     request=request, user=user)
#                 return Response(user_details, status=status.HTTP_200_OK)
#
#             except Exception as e:
#                 raise e
#         else:
#             res = {
#                 'error': 'can not authenticate with the given credentials or the account has been deactivated'}
#             return Response(res, status=status.HTTP_403_FORBIDDEN)
#     except KeyError:
#         res = {'error': 'please provide a email and a password'}
#         return Response(res)
#
# #ХЗ что и куда
# user_logged_in.send(sender=user.__class__, request=request, user=user)
#
# # user/views
# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     # Allow only authenticated users to access this url
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserSerializer
#
#     def get(self, request, *args, **kwargs):
#         # serializer to handle turning our `User` object into something that
#         # can be JSONified and sent to the client.
#         serializer = self.serializer_class(request.user)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, *args, **kwargs):
#         serializer_data = request.data.get('user', {})
#
#         serializer = UserSerializer(
#             request.user, data=serializer_data, partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_200_OK)



#Тренировочний клас*************************************************************

# class PostView(mixin.ListModelMixin, mixin.CreateModelMixin, generics.GenericAPIView,):
#     serializer_class = CarDetailSerializer
#     queryset = Post.object.all()
#     """Получае метод Гет етим расширением"""
#     def get(self, request, *args, **kwargs):
#         return self.list(self, request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.list(self, request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         #send on email
#         serializer.save()

# class TestViews(APIView):
#         """Реализовали 2-а метода Get и Post"""
#
#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         post = qs.first()
#         #serializer = PostSerializer(qs, many=True)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)