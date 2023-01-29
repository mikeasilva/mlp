import pytest
from mlp import data

def test_generate_soap_notes_raises_value_error_with_big_number():
    with pytest.raises(ValueError, match="Too many SOAP notes requested!"):
        data.generate_soap_notes(1000000)

def test_generate_soap_notes_raises_value_error_with_negative_number():
    with pytest.raises(ValueError, match="Too few SOAP notes requested!"):
        data.generate_soap_notes(-1)

def test_generate_soap_notes_raises_type_error_when_junk_passed_in():
    error = "n must be an int. Received a "
    with pytest.raises(TypeError, match=error + "str"):
        data.generate_soap_notes("1")
    with pytest.raises(TypeError, match=error + "dict"):
        data.generate_soap_notes({"1":"1"})
    with pytest.raises(TypeError, match=error + "list"):
        data.generate_soap_notes([1])
    with pytest.raises(TypeError, match=error + "float"):
        data.generate_soap_notes(1/2)

    # Pass in invalid anonymize_patient
    error = "anonymize_patient must be a bool. Received a "
    with pytest.raises(TypeError, match=error + "str"):
        data.generate_soap_notes(1, anonymize_patient = "1")
    with pytest.raises(TypeError, match=error + "dict"):
        data.generate_soap_notes(1, anonymize_patient = {"1":"1"})
    with pytest.raises(TypeError, match=error + "list"):
        data.generate_soap_notes(1, anonymize_patient = [1])
    with pytest.raises(TypeError, match=error + "float"):
        data.generate_soap_notes(1, anonymize_patient = 1/2)

    # Pass in invalid use_full_section_headers
    error = "use_full_section_headers must be a bool. Received a "
    with pytest.raises(TypeError, match=error + "str"):
        data.generate_soap_notes(1, use_full_section_headers = "1")
    with pytest.raises(TypeError, match=error + "dict"):
        data.generate_soap_notes(1, use_full_section_headers = {"1":"1"})
    with pytest.raises(TypeError, match=error + "list"):
        data.generate_soap_notes(1, use_full_section_headers = [1])
    with pytest.raises(TypeError, match=error + "float"):
        data.generate_soap_notes(1, use_full_section_headers = 1/2)


def test_generate_soap_notes_returns_a_list():
    assert isinstance(data.generate_soap_notes(1), list)

def test_generate_soap_notes_returns_correct_number_of_notes_in_a_list():
    assert len(data.generate_soap_notes(1)) == 1
    assert len(data.generate_soap_notes(2)) == 2

def test_generate_soap_notes_replaces_template_placeholders():
    soap_note = data.generate_soap_notes(1)[0]
    n_characters = len(soap_note)
    assert len(soap_note.replace("[subjective]", "")) == n_characters
    assert len(soap_note.replace("[objective]", "")) == n_characters
    assert len(soap_note.replace("[assessment]", "")) == n_characters
    assert len(soap_note.replace("[plan]", "")) == n_characters