from rest_framework import routers
from django.urls import path
from classes.apps import ClassesConfig


from classes.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView, \
    SubscriptionCreateAPIView, SubscriptionRetrieveAPIView, SubscriptionUpdateAPIView, SubscriptionDestroyAPIView

app_name = ClassesConfig.name

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson_view'),
    path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    # payment
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/<int:pk>', PaymentRetrieveAPIView.as_view(), name='payment_view'),
    # subscription
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/<int:pk>', SubscriptionRetrieveAPIView.as_view(), name='subscription_view'),
    path('subscription/update/<int:pk>', SubscriptionUpdateAPIView.as_view(), name='subscription_update'),
    path('subscription/delete/<int:pk>', SubscriptionDestroyAPIView.as_view(), name='subscription_delete')

] + router.urls
