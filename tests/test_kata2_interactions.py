from katas import kata2_interactions
import pytest
from testfixtures import LogCapture

@pytest.fixture(autouse=True)
def capture():
    with LogCapture() as capture:
        yield capture

def test_add_logged(capture):
    kata2_interactions.str_add("")
    capture.check(('str_add', 'INFO', '0'))

def test_add_logged_error(capture):
    with pytest.raises(AssertionError):
        kata2_interactions.str_add("-1")

    capture.check(('str_add', 'ERROR', "['-1']"))