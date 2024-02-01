import pytest
from rest_framework.test import APIClient

from students.models import Student, Course
from model_bakery import baker


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory2(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory2


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_api_get_first(client, course_factory):
    courses = course_factory(_quantity=10, make_m2m=True)
    response = client.get('/api/v1/courses/1/')
    data = response.json()
    assert response.status_code == 200
    assert courses[0].name == data['name']


@pytest.mark.django_db
def test_api_filter_course_id(client, course_factory):
    courses = course_factory(_quantity=10, make_m2m=True)
    response = client.get('/api/v1/courses/', {'id': 12})
    data = response.json()
    assert response.status_code == 200
    assert courses[1].name == data[0]['name']


@pytest.mark.django_db
def test_api_get_courses(client, course_factory):
    courses = course_factory(_quantity=10, make_m2m=True)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    assert len(courses) == len(data)
    for item, course in enumerate(data):
        assert course['name'] == courses[item].name


@pytest.mark.django_db
def test_api_filter_course_name(client, course_factory):
    courses = course_factory(_quantity=10, make_m2m=True)
    response = client.get('/api/v1/courses/', {'name': courses[2].name})
    data = response.json()
    assert response.status_code == 200
    assert courses[2].name == data[0]['name']


@pytest.mark.django_db
def test_api_create_course(client):
    count = Course.objects.all().count()
    response = client.post('/api/v1/courses/', {'name': 'Math'})
    assert Course.objects.all().count() == count + 1
    assert response.status_code == 201
    assert Course.objects.all().count() == count + 1
    assert Course.objects.get(name=response.json()['name']).name == response.json()['name']

@pytest.mark.django_db
def test_api_update(client, course_factory):
    courses = course_factory(_quantity=10, make_m2m=True)
    response = client.patch('/api/v1/courses/45/', {'name': 'Physics'})
    data = response.json()
    assert response.status_code == 200
    assert Course.objects.get(name=data['name']).name == data['name']
    assert Course.objects.all().count() == len(courses)


@pytest.mark.django_db
def test_api_remove(client, course_factory):
    courses = course_factory(_quantity=10, make_m2m=True)
    response = client.delete('/api/v1/courses/55/')
    assert response.status_code == 204
    assert Course.objects.all().count() == len(courses) - 1
