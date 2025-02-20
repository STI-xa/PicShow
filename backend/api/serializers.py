from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from users.validators import validate_username, validate_password
from users.models import User
from pics.models import Photo, Tag, Category, Comment


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'is_staff',
                  'is_active',
                  'date_joined')


class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta:
        model = User
        fields = User.REQUIRED_FIELDS

    def validate_username(self, value):
        return validate_username(value)

    def validate_password(self, value):
        return validate_password(value)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    photo = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class PhotoListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    author = CustomUserSerializer(read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    image = serializers.ImageField(max_length=None, allow_empty_file=False)

    class Meta:
        model = Photo
        fields = '__all__'


class PhotoCreateSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        many=True,
        queryset=Category.objects.all()
    )
    tag = serializers.SlugRelatedField(
        slug_field='slug',
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Photo
        fields = '__all__'
