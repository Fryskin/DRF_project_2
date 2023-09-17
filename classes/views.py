from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from classes.models import Course, Lesson, Payment, Subscription
from classes.paginators import ClassesPaginator
from classes.permissions import IsStaff, IsOwner
from classes.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer
from rest_framework.response import Response
import stripe


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

        stripe.api_key = "sk_test_51NrK4fC6CMlyHByPNz3BIrLoBUdUNQTP6smWQNord9uOdkMfP65XhGxa7q3aYxCgxZaVVYR9lB9fnhZyz844BYYD00QKY1sR8K"

        stripe.Price.create(
            unit_amount=120,
            currency="usd",
            recurring={"interval": "month"},
            product="prod_OUtWghl8cgKm7R",
        )

        stripe.checkout.Session.create(
            success_url="https://example.com/success",
            line_items=[
                {
                    "price": "price_H5ggYwtDq4fbrJ",
                    "quantity": 2,
                },
            ],
            mode="subscription",
        )


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
