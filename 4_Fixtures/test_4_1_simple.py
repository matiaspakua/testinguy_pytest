import sys

import pytest

import pytest

@pytest.fixture
def students_sample_marks():
    return [
        {
            "name": "john",
            "id": 1,
            "subject": "English",
            "mark": 39,
        },
        {
            "name": "jane",
            "id": 5,
            "subject": "English",
            "mark": 45,
        },
        {
            "name": "rick",
            "id": 100,
            "subject": "English",
            "mark": 36,
        },
        ]

def get_student_details_by_property(student_data, property_name):
    return list(map(lambda x: f"{x.get('name')}: {x.get(property_name)}",student_data))

def test_name_and_mark_display(students_sample_marks):
    assert get_student_details_by_property(students_sample_marks,'mark') == ['john: 39', 'jane: 45', 'rick: 36']

def test_name_and_id_display(students_sample_marks):
    assert get_student_details_by_property(students_sample_marks,'id') == ['john: 1', 'jane: 5', 'rick: 100']