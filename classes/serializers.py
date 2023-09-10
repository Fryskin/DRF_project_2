from rest_framework import serializers

from classes.models import Course, Lesson, Payment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(source='lesson_set.all.lesson', read_only=True)
    lesson = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = ['title', 'description', 'preview', 'lessons_count']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

