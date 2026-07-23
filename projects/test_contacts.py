import os

from contacts import count_contacts, load_contacts, save_contacts


def test_count_empty():
    assert count_contacts({}) == 0


def test_count_multiple():
    assert count_contacts({"Alice": "123", "Bob": "456"}) == 2


def test_count_ignores_value_type():
    assert count_contacts({"Alice": ""}) == 1


def test_save_and_load_round_trip(tmp_path):
    file_path = str(tmp_path / "contacts.json")
    original = {"Alice": "123", "Bob": "456"}
    save_contacts(original, file_path)
    assert load_contacts(file_path) == original


def test_load_missing_file_returns_empty(tmp_path):
    file_path = str(tmp_path / "does_not_exist.json")
    assert load_contacts(file_path) == {}


def test_load_corrupt_file_returns_empty(tmp_path):
    file_path = str(tmp_path / "contacts.json")
    with open(file_path, "w") as corrupt_file:
        corrupt_file.write("this is not valid json {")
    assert load_contacts(file_path) == {}


def test_load_non_dict_json_returns_empty(tmp_path):
    file_path = str(tmp_path / "contacts.json")
    with open(file_path, "w") as list_file:
        list_file.write("[1, 2, 3]")
    assert load_contacts(file_path) == {}
