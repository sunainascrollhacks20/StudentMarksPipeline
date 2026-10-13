
import pytest

from student_marks import (
    calculate_total,
    calculate_percentage,
    get_result,
)


def test_calculate_total():
    assert calculate_total([75, 80, 65]) == 220


def test_calculate_percentage():
    assert calculate_percentage([75, 80, 65]) == pytest.approx(
        73.3333333333
    )


def test_pass_result():
    assert get_result([75, 80, 65]) == "Pass"


def test_fail_result():
    assert get_result([75, 30, 65]) == "Fail"


def test_invalid_number_of_subjects():
    with pytest.raises(ValueError):
        calculate_total([75, 80])


def test_invalid_marks():
    with pytest.raises(ValueError):
        calculate_total([75, 120, 65])
