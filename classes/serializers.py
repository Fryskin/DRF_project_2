from rest_framework import serializers

from classes.models import Course, Lesson, Payment, Subscription

from classes.validators import VideoURLValidator, DescriptionValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoURLValidator(field='video_url'), DescriptionValidator(field='description')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(source='lesson_set.all.lesson', read_only=True)
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['title', 'description', 'preview', 'lessons_count', 'lesson']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
