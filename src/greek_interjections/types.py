"""
Linting types
"""
from typing import TypedDict, Optional, List, Union


class DiorisisLemma(TypedDict):
    """
    TODO
    """

    id: str
    entry: str
    POS: Optional[str]
    disambiguated: str
    TreeTagger: str
    analyses: List[Optional[str]]


class DiorisisTokens(TypedDict):
    """
    TODO
    """

    type: str
    form: str
    id: Optional[str]
    lemma: Optional[DiorisisLemma]


class DiorisisSentence(TypedDict):
    """
    TODO
    """

    id: str
    location: str
    tokens: List[Union[DiorisisTokens]]


class DiorisisDocument(TypedDict):
    """
    TODO
    """

    sentences: List[DiorisisSentence]
    version: str
