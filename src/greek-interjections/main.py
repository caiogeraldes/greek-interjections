"""
TODO
"""
import os
from dotenv import load_dotenv

load_dotenv()

DIORISIS_PATH = os.getenv("DIORISIS_PATH")
assert DIORISIS_PATH is not None, "Path para DIORISIS não especificada"
