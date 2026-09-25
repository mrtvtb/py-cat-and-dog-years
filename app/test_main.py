from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_years, dog_years, result", [
    (0, 0, [0, 0]),
    (15, 15, [1, 1]),
    (24, 24, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
], ids=[
    "zero_years",
    "first_boundary",
    "second_year",
    "third_year",
    "old_pet"
])
def test_get_human_age(cat_years: int, dog_years: int, result: list) -> None:
    assert get_human_age(cat_years, dog_years) == result
