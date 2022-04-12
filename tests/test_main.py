import os
import pytest
from greek_interjections.main import main

FIXTURE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/")

@pytest.mark.datafiles(os.path.join(FIXTURE_DIR))
def test_main(datafiles):
    os.environ["DIORISIS_PATH"] = os.path.join(datafiles, "json/")
    os.environ["DATA_PATH"] = os.path.join(datafiles)
    main()
