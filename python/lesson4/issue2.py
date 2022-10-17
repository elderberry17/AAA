import pytest

from issue1 import decode


@pytest.mark.parametrize(
    "code,result",
    [
        ('... --- ...', 'SOS'),
        ('-..- -.-- --..', 'XYZ'),
        ('-.- .-  .. ..-. ', 'KAIF')
    ]
)
def test_decode(code, result):
    assert decode(code) == result
