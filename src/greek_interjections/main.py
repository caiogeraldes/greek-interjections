"""
TODO
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from greek_interjections.tools import gen_dataframe
from greek_interjections.query_diorisis import bulk_find

load_dotenv()

diorisis_path = os.getenv("DIORISIS_PATH")
assert diorisis_path is not None, "Path para DIORISIS não especificada"
DIORISIS_PATH = Path(diorisis_path)
data_path = os.getenv("DATA_PATH")
assert data_path is not None, "Path para DATA não especificada"
DATA_PATH = Path(data_path)


if __name__ == "__main__":  # pragma: no cover
    results = bulk_find(DIORISIS_PATH)
    data_frame = gen_dataframe(results)
    data_frame.to_csv(os.path.join(DATA_PATH, "data.csv"), index=False)
