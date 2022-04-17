"""
TODO
"""
from typing import List, Optional
import pandas as pd
import regex
from greek_interjections.diorisistypes import DiorisisSentence
from greek_interjections.beta_to_unicode import BetaCodeReplacer


def gen_sentence(sentence: DiorisisSentence) -> str:
    """
    Generates a string from a sentence object produced from a Diorisis query
    @param sentence:
    @return:
    """
    replacer = BetaCodeReplacer()
    sentence_string: str = ""
    for token in sentence["tokens"]:
        sentence_string += replacer.replace_beta_code(token["form"]) + " "

    # Clean spacing
    sentence_string = sentence_string.strip()
    sentence_string = regex.sub(r"\ ([·,.;ʼ])", r"\1", sentence_string)
    return sentence_string


def gen_dataframe(data: List[dict[str, Optional[str]]]) -> pd.DataFrame:
    """
    Generate a dataframe
    @param data:
    @return:
    """
    data_frame = pd.DataFrame(data)
    return data_frame
