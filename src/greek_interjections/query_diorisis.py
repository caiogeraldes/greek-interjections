"""
TODO
"""
import os
import json
from os import PathLike
from typing import List, Optional
import regex
from greek_interjections.types import DiorisisDocument, DiorisisSentence
from greek_interjections.tools import gen_sentence
from greek_interjections.beta_to_unicode import BetaCodeReplacer


def find_interjections(diorisis_json: str) -> List[dict[str, Optional[str]]]:
    """
    TODO
    @param diorisis_json: str
    @return:
    """
    with open(diorisis_json, "r", encoding="utf-8") as file:
        document: DiorisisDocument = json.load(file)

    sentence_ids = []
    tokens = []
    tokens_position = []

    author: str
    text: str
    author, text = os.path.basename(diorisis_json).split("-")
    author = regex.sub(r"\ \(\d+\)", "", author.strip())
    text = regex.sub(r"\ \(\d+\)", "", text.strip())
    text = regex.sub(r"\.json", "", text)

    for sentence in document["sentences"]:
        for token in sentence["tokens"]:
            if token["type"] != "word":
                continue
            if token["lemma"]:
                if "POS" not in list(token["lemma"].keys()):
                    continue
                if token["lemma"]["POS"] == "interjection":
                    tokens.append(token["form"])
                    tokens_position.append(token["id"])
                    sentence_ids.append(sentence["id"])

    hits = []
    conv = BetaCodeReplacer()
    for _token, token_position, sentence_id in zip(
        tokens, tokens_position, sentence_ids
    ):
        hits.append(
            {
                "author": author,
                "text": text,
                "location": get_location(document["sentences"][int(sentence_id) - 1]),
                "interjection": conv.replace_beta_code(_token),
                "sentence_position": token_position,
                "sentence": gen_sentence(document["sentences"][int(sentence_id) - 1]),
            }
        )
    return hits


def get_location(diorisis_sent: DiorisisSentence) -> str:
    """
    TODO
    @param diorisis_sent:
    @return:
    """
    return diorisis_sent["location"]


def bulk_find(diorsis_path: PathLike) -> List[dict[str, Optional[str]]]:
    """
    TODO
    @param diorsis_path: path to Diorisis collection
    @return:
    """
    file_list = os.listdir(diorsis_path)
    texts = []
    for file in file_list:
        if file == "corpus.json":
            continue
        for hit in find_interjections(os.path.join(diorsis_path, file)):
            texts.append(hit)
    return texts
