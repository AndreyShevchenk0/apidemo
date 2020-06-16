from rest_framework import generics
from demopost.serializers import PostDetailSerializer, PostListSerializer, PostCreateSerializer
from demopost.models import Post
from demopost.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class PostCreateView(generics.CreateAPIView,):
    """ Создание Записи """
    serializer_class = PostDetailSerializer


class PostListView(generics.ListAPIView):
    """ Просмотр всех записей  Пользователя """
    serializer_class = PostListSerializer
    queryset = Post.objects.all()#filter(update_post=timezone.now())  # фильт рdates('added_post', 'day')
    permission_classes = (IsAuthenticated,)

class PostDetailView(generics. RetrieveUpdateDestroyAPIView):
    """ Просмотр конкретних записей, редактирование и удаление! """
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)



    # class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    #     """ Просмотр конкретних записей, редактирование и удаление! +
    #     Просмотр всех записей за последние 15 дней Пользователя """
    #     serializer_class = PostDetailSerializer
    #     queryset = Post.objects.all().filter('id','-update_post')
    #     #queryset = Post.objects.all(id=current_post).filter(author=user)
                                        #.order_by('-update_post')#.all #(id=current_post)
    #     permission_classes = (IsOwnerOrReadOnly,)



    #pip install django-filter
    #from django_filters.rest_framework import DjangoFilterBackend
    # разкоментировать в сетингах
    # class ProductList(generics.ListAPIView):
    #     queryset = Product.objects.all()
    #     serializer_class = ProductSerializer
    #     filter_backends = [DjangoFilterBackend]
    #     filterset_fields = ['id'= -15, + 'update_post' = -15 ]


    #name = 'coment_list'
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


#JWT user/views
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
# #
# #ХЗ что и куда
# user_logged_in.send(sender=user.__class__, request=request, user=user)
