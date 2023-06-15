import pytest
from main import get_ifo_about_user, get_year_user, get_age_user, hello_user


@pytest.mark.parametrize(
    ('name', 'age', 'result'), [
        ('Lisa', 20, 'Hello, Lisa! You are 20. You were born in 2003.'),
        ('Vasya', 5, 'Hello, Vasya! You are 5. You were born in 2018.'),
        ('Petya', 55, 'Hello, Petya! You are 55. You were born in 1968.'),
    ]
)
def test_get_user_info(name, age, result):
    assert get_ifo_about_user(name, age) == result

@pytest.mark.parametrize(
    ('name', 'result'), [
        ('Lisa','Hello, Lisa! '),
        ('Vasya', 'Hello, Vasya! '),
        ('Petya', 'Hello, Petya! '),
    ]
)
def test_get_user_name(name, result):
    assert hello_user(name) == result

@pytest.mark.parametrize(
    ('age', 'result'), [
        (15,'You were born in 2008.'),
        (67, 'You were born in 1956.'),
        (89, 'You were born in 1934.'),
    ]
)
def test_get_user_year(age, result):
    assert get_year_user(age) == result

@pytest.mark.parametrize(
    ('age', 'result'), [
        (15,'You are 15. '),
        (67, 'You are 67. '),
        (89, 'You are 89. '),
    ]
)
def test_get_user_age(age, result):
    assert get_age_user(age) == result