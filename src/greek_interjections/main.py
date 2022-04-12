"""
TODO
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from greek_interjections.tools import gen_dataframe
from greek_interjections.query_diorisis import bulk_find


def main():
    """
    TODO
    @return:
    """
    load_dotenv()

    diorisis_path = os.getenv("DIORISIS_PATH")
    assert diorisis_path is not None, "Path para DIORISIS não especificada"
    diorisis_path = Path(diorisis_path)
    data_path = os.getenv("DATA_PATH")
    assert data_path is not None, "Path para DATA não especificada"
    data_path = Path(data_path)

    results = bulk_find(diorisis_path)
    data_frame = gen_dataframe(results)
    data_frame.to_csv(os.path.join(data_path, "data.csv"), index=False)


if __name__ == "__main__":  # pragma: no cover
    main()
