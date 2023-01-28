import pytest
from MLP import data

def test_data_generate_soap_notes_raises_value_error_with_big_number():
    with pytest.raises(ValueError, match="Too many SOAP notes requested!"):
        data.generate_soap_notes(1000000)

def test_data_generate_soap_notes_raises_value_error_with_negative_number():
    with pytest.raises(ValueError, match="Too few SOAP notes requested!"):
        data.generate_soap_notes(-1)

def test_data_generate_soap_notes_raises_type_error_when_junk_passed_in():
    error = "Expected int. Received "
    with pytest.raises(TypeError, match=error + "str"):
        data.generate_soap_notes("1")
    with pytest.raises(TypeError, match=error + "dict"):
        data.generate_soap_notes({"1":"1"})

def test_data_generate_soap_notes_returns_a_list():
    assert isinstance(data.generate_soap_notes(1), list)
'''
def test_data_generate_soap_notes_returns_correct_number_of_notes_in_a_list():
    assert len(data.generate_soap_notes(1)) == 1
    assert len(data.generate_soap_notes(2)) == 2
'''