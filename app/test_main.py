from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_years, dog_years, result", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (15, 24, [1, 2]),
], ids=[
    "zero_years",
    "fourteen_age",
    "first_boundary",
    "twenty_three_age",
    "second_year",
    "twenty_seven_age",
    "third_year",
    "old_pet",
    "mixed_years",
])
def test_get_human_age(cat_years: int, dog_years: int, result: list) -> None:
    assert get_human_age(cat_years, dog_years) == result
