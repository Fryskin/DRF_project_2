import webbrowser

from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from classes.models import Course, Lesson, Payment, Subscription
from classes.paginators import ClassesPaginator
from classes.permissions import IsStaff, IsOwner
from classes.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer
from rest_framework.response import Response
import stripe

from classes.tasks import update_of_course_mailing


class CourseViewSet(viewsets.ModelViewSet):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    # permission_classes = [IsOwner]
    pagination_class = ClassesPaginator


class LessonCreateAPIView(generics.CreateAPIView):
    """ Create Lesson """
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """ List Lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsOwner]
    pagination_class = ClassesPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """ Retrieve Lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """ Update Lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsStaff, IsOwner]

    def perform_update(self, serializer):
        mailing = serializer.save()
        update_of_course_mailing.delay('User')


class LessonDestroyAPIView(generics.DestroyAPIView):
    """ Destroy Lesson """
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class PaymentCreateAPIView(generics.CreateAPIView):
    """ Create Payment """
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    """ List Payment """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course_paid', 'type_of_payment')
    ordering_fields = ('date_of_payment',)


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    """ Retrieve Payment """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """ Create Subscription """
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        new_subscription = serializer.save()
        new_subscription.save()

        webbrowser.open('https://checkout.stripe.com/c/pay/cs_test_a1yIDHj78YjSES9r5m9qynuwy27b6Lnzi8HFtXWCLYaP21Nhm'
                        'F85A5ZdIc#fidkdWxOYHwnPyd1blpxYHZxWjA0S3dOMWNGM0ZIaXxNR3xVV3NRPGhSMjxAVWRkfGw2Xz1sXVREZ000N'
                        '219SWwxfHcxckxsXXVQbGdrbWhjVHJ9QjFwUXxmalBka042R3Vic1MxbVNPVHN8NTVUcUZXQDJ0YCcpJ2N3amhWYHdz'
                        'YHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl', new=1)


class SubscriptionRetrieveAPIView(generics.RetrieveAPIView):
    """ Retrieve Subscription """
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsOwner]


class SubscriptionUpdateAPIView(generics.UpdateAPIView):
    """ Update Subscription """
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsOwner]


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """ Destroy Subscription """
    queryset = Subscription.objects.all()
    permission_classes = [IsOwner]
