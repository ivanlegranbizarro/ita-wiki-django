import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

pytestmark = pytest.mark.django_db

User = get_user_model()


def test_create_user():
    user = User.objects.create_user(
        '12345678A', 'testuser@example.com', 'password')
    assert user.email == 'testuser@example.com'
    assert user.is_active
    assert not user.is_admin
    assert not user.is_staff


def test_create_user_no_dni():
    with pytest.raises(ValueError):
        User.objects.create_user(None, 'testuser@example.com', 'password')


def test_create_user_no_email():
    with pytest.raises(ValueError):
        User.objects.create_user('12345678A', None, 'password')


def test_create_user_duplicate_dni():
    User.objects.create_user('12345678A', 'testuser@example.com', 'password')
    with pytest.raises(IntegrityError):
        User.objects.create_user(
            '12345678A', 'testuser2@example.com', 'password')


def test_create_superuser():
    user = User.objects.create_superuser(
        '12345678A', 'testuser@example.com', 'password')
    assert user.email == 'testuser@example.com'
    assert user.is_active
    assert user.is_admin
    assert user.is_staff


def test_dni_validation():
    with pytest.raises(ValidationError):
        user = User(dni='123456789', email='testuser@example.com')
        user.full_clean()

    with pytest.raises(ValidationError):
        user = User(dni='12345678', email='testuser@example.com')
        user.full_clean()

    with pytest.raises(ValidationError):
        user = User(dni='12345678AB', email='testuser@example.com')
        user.full_clean()


def test_user_str_method():
    user = User.objects.create_user(
        '12345678A', 'testuser@example.com', 'password')
    assert str(user) == '12345678A'
