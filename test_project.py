import pytest
from project import is_valid_status, load_jobs


def test_is_valid_status_valid():
    assert is_valid_status("Interested") is True
    assert is_valid_status("Applied") is True
    assert is_valid_status("Interviewing") is True
    assert is_valid_status("Offer") is True
    assert is_valid_status("Rejected") is True


def test_is_valid_status_invalid():
    assert is_valid_status("Done") is False
    assert is_valid_status("Pending") is False
    assert is_valid_status("Hired") is False


def test_load_jobs_file_not_found():
    assert load_jobs("missing_file.json") == []


def test_load_jobs_bad_json(tmp_path):
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("not valid json")
    assert load_jobs(str(bad_file)) == []