import pytest

from page_loader.loader import load_data
from tests import FIXTURES, read_file


@pytest.mark.parametrize(
    argnames="url",
    argvalues=["https://ru.hexlet.io/courses"]
)
def test_load_data(url, requests_mock):
    """
    Test for load_data function

    :param url: page url
    :param requests_mock: requests_mock object
    :return:
    """
    expected = read_file(FIXTURES / "ru-hexlet-io-courses.html")
    requests_mock.get(url, text=expected)
    got = load_data(url).decode("utf-8")

    assert got == expected
