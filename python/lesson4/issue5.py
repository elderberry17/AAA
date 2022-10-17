import json
from unittest.mock import MagicMock

import pytest

from what_is_year_now import what_is_year_now


def test_wrong():
    with pytest.raises(ValueError):
        json.load = MagicMock(return_value={"currentDateTime": "07/10/2022"})
        what_is_year_now()


def test_line():
    json.load = MagicMock(return_value={"currentDateTime": "2022-10-07"})
    assert 2022 == what_is_year_now()


def test_point():
    json.load = MagicMock(return_value={"currentDateTime": "07.10.2022"})
    assert 2022 == what_is_year_now()
