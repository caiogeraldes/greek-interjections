import os
import pytest
from greek_interjections.query_diorisis import find_interjections, bulk_find

pytest_plugins = "pytester"

TEST_DOC = "Euripides (0006) - Electra (042).json"

FIXTURE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/json/")


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, TEST_DOC))
def test_find_interjections(datafiles):
    diofile: str = str(os.path.join(datafiles, TEST_DOC))
    output = find_interjections(diofile)
    assert len(output) == 102


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR))
def test_bulk_find(datafiles):
    output = bulk_find(datafiles)
    assert len(output) == 102 + 77
