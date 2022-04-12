from greek_interjections.tools import gen_sentence


def test_gen_sentence():
    source = {
        "id": "1",
        "location": "1",
        "tokens": [
            {
                "type": "word",
                "form": "w)=",
                "id": "1",
                "lemma": {
                    "id": "116027",
                    "entry": "w)=",
                    "POS": "interjection",
                    "disambiguated": "1.0",
                    "TreeTagger": "true",
                    "analyses": ["indeclform (exclam)"],
                },
            },
            {
                "type": "word",
                "form": "gh=s",
                "id": "2",
                "lemma": {
                    "id": "22100",
                    "entry": "gh=",
                    "POS": "noun",
                    "disambiguated": "1.0",
                    "TreeTagger": "true",
                    "analyses": ["fem gen sg (attic epic ionic)"],
                },
            },
            {
                "type": "word",
                "form": "palaio\\n",
                "id": "3",
                "lemma": {
                    "id": "76765",
                    "entry": "palaio/s",
                    "POS": "adjective",
                    "TreeTagger": "false",
                    "disambiguated": "n/a",
                    "analyses": ["masc acc sg", "neut nom/voc/acc sg"],
                },
            },
            {
                "type": "word",
                "form": "a)/rgos",
                "id": "4",
                "lemma": {
                    "id": "unknown",
                    "TreeTagger": "false",
                    "disambiguated": "n/a",
                    "analyses": [],
                },
            },
            {"type": "punct", "form": ","},
            {
                "type": "word",
                "form": "*)ina/xou",
                "id": "5",
                "lemma": {
                    "id": "50498",
                    "entry": "*)/inaxos",
                    "POS": "proper",
                    "TreeTagger": "false",
                    "disambiguated": "n/a",
                    "analyses": ["masc gen sg"],
                },
            },
            {
                "type": "word",
                "form": "r(oai/",
                "id": "6",
                "lemma": {
                    "id": "92633",
                    "entry": "r(oh/",
                    "POS": "noun",
                    "TreeTagger": "false",
                    "disambiguated": "n/a",
                    "analyses": ["fem nom/voc pl"],
                },
            },
            {"type": "punct", "form": ","},
            {
                "type": "word",
                "form": "o(/qen",
                "id": "7",
                "lemma": {
                    "id": "72153",
                    "entry": "o(/qen",
                    "POS": "adverb",
                    "TreeTagger": "false",
                    "disambiguated": "n/a",
                    "analyses": ["indeclform (adverb)"],
                },
            },
            {
                "type": "word",
                "form": "pot'",
                "id": "8",
                "lemma": {
                    "id": "nlsj67563",
                    "entry": "pote/",
                    "POS": "particle",
                    "disambiguated": "1.0",
                    "TreeTagger": "true",
                    "analyses": [
                        "aeolic (enclitic indeclform particle)",
                        "enclitic indeclform (particle)",
                    ],
                },
            },
            {
                "type": "word",
                "form": "a)/ras",
                "id": "9",
                "lemma": {
                    "id": "2660",
                    "entry": "ai)/rw",
                    "POS": "verb",
                    "TreeTagger": "false",
                    "disambiguated": "n/a",
                    "analyses": [
                        "aor part act masc nom/voc sg (attic epic doric ionic aeolic)"
                    ],
                },
            },
            {
                "type": "word",
                "form": "nausi\\",
                "id": "10",
                "lemma": {
                    "id": "69863",
                    "entry": "nau=s",
                    "POS": "noun",
                    "TreeTagger": "false",
                    "disambiguated": "n/a",
                    "analyses": ["dat pl (attic)", "fem dat pl (doric)"],
                },
            },
            {
                "type": "word",
                "form": "xili/ais",
                "id": "11",
                "lemma": {
                    "id": "114005",
                    "entry": "xi/lioi",
                    "POS": "adjective",
                    "disambiguated": "0.5",
                    "TreeTagger": "true",
                    "analyses": ["fem dat pl"],
                },
            },
            {
                "type": "word",
                "form": "*)/arh",
                "id": "12",
                "lemma": {
                    "id": "14990",
                    "entry": "*)/arhs",
                    "POS": "proper",
                    "disambiguated": "0.5",
                    "TreeTagger": "false",
                    "analyses": ["masc acc sg", "masc voc sg (epic)"],
                },
            },
            {
                "type": "word",
                "form": "e)s",
                "id": "13",
                "lemma": {
                    "id": "31235",
                    "entry": "ei)s",
                    "POS": "preposition",
                    "TreeTagger": "false",
                    "disambiguated": "n/a",
                    "analyses": ["proclitic indeclform (prep)"],
                },
            },
            {
                "type": "word",
                "form": "gh=n",
                "id": "14",
                "lemma": {
                    "id": "22100",
                    "entry": "gh=",
                    "POS": "noun",
                    "disambiguated": "1.0",
                    "TreeTagger": "true",
                    "analyses": ["fem acc sg (attic epic ionic)"],
                },
            },
            {
                "type": "word",
                "form": "e)/pleuse",
                "id": "15",
                "lemma": {
                    "id": "83754",
                    "entry": "ple/w",
                    "POS": "verb",
                    "TreeTagger": "false",
                    "disambiguated": "n/a",
                    "analyses": ["aor ind act 3rd sg"],
                },
            },
            {
                "type": "word",
                "form": "*trw|a/d",
                "id": "16",
                "lemma": {
                    "id": "unknown",
                    "TreeTagger": "false",
                    "disambiguated": "n/a",
                    "analyses": [],
                },
            },
            {"type": "punct", "form": ")"},
            {
                "type": "word",
                "form": "*)agame/mnwn",
                "id": "17",
                "lemma": {
                    "id": "317",
                    "entry": "*)agame/mnwn",
                    "POS": "proper",
                    "TreeTagger": "false",
                    "disambiguated": "n/a",
                    "analyses": ["masc nom/voc sg"],
                },
            },
            {
                "type": "word",
                "form": "a)/nac",
                "id": "18",
                "lemma": {
                    "id": "7094",
                    "entry": "a)/nac",
                    "POS": "noun",
                    "TreeTagger": "false",
                    "disambiguated": "n/a",
                    "analyses": ["masc nom/voc sg"],
                },
            },
            {"type": "punct", "form": "."},
        ],
    }
    expected = (
        "ὦ γῆς παλαιὸν ἄργος, Ἰνάχου ῥοαί, "
        "ὅθεν ποτʼ ἄρας ναυσὶ χιλίαις Ἄρη ἐς γῆν ἔπλευσε Τρῳάδ ̓ Ἀγαμέμνων ἄναξ."
    )
    output = gen_sentence(source)
    assert output == expected
