from rest_framework import status
from rest_framework.test import APITestCase

from classes.models import Course, Lesson, Payment


class ClassesTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_create_course(self):
        """ The Testcase of creating the course """
        data = {
            "title": "Python",
            "description": "For you"
        }

        response = self.client.post(
            '/courses/',
            data=data

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'title': 'Python', 'description': 'For you', 'preview': None, 'lesson': []}
        )

        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_list_course(self):
        """ The Testcase of course list's output """
        Course.objects.create(
            title='Jojo',
            description='Bizarre Adventure 300$'
        )

        response = self.client.get(
            '/courses/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None,
             'results': [{'title': 'Jojo', 'description': 'Bizarre Adventure 300$', 'preview': None, 'lesson': []}]}
        )

    def test_create_lesson(self):
        """ The Testcase of creating the lesson """
        Course.objects.create(
            title='Jojo',
            description='Bizarre Adventure 300$'
        )

        data = {
            'id': 1,
            "title": "АСМР",
            "description": "Привет",

            "video_url": "https://www.youtube.com/watch?v=N2-r9vNRHRg",
            "course": [1]
        }

        response = self.client.post(
            '/lesson/create/',
            data=data

        )
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'title': 'АСМР', 'description': 'Привет', 'preview': None, "user": None,
             "video_url": "https://www.youtube.com/watch?v=N2-r9vNRHRg", "course": [1]}
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        Lesson.objects.create(
            id=1,
            title="АСМР",
            description="Привет",

            video_url="https://www.youtube.com/watch?v=N2-r9vNRHRg"


        )

        response = self.client.get(
            '/lesson/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [{'id': 1, 'title': 'АСМР', 'description': 'Привет',
             'preview': None, 'video_url': 'https://www.youtube.com/watch?v=N2-r9vNRHRg', 'user': None, 'course': []}]}
        )

    def test_create_payment(self):
        """ The Testcase of creating the payment """
        Course.objects.create(
            title='Jojo',
            description='Bizarre Adventure 300$'
        )

        data = {
            'date_of_payment': '2020-11-28T19:24:58.478641+05:30',
            "course_paid": 1,
            "payment_amount": 300,
            "type_of_payment": "Cash"
        }

        response = self.client.post(
            '/payment/create/',
            data=data

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'date_of_payment': '2020-11-28T13:54:58.478641Z', 'payment_amount': 300,
             'type_of_payment': 'Cash', 'user': None, 'course_paid': 1}
        )

        self.assertTrue(
            Payment.objects.all().exists()
        )

    def test_list_payment(self):
        Payment.objects.create(

            date_of_payment='2020-11-28T19:24:58.478641Z',

            payment_amount=300,
            type_of_payment="Cash"

        )

        response = self.client.get(
            '/payment/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 1, 'date_of_payment': '2020-11-28T19:24:58.478641Z', 'payment_amount': 300,
              'type_of_payment': "Cash", 'user': None, 'course_paid': None}]
        )
