from greek_interjections.beta_to_unicode import BetaCodeReplacer


def test_replace_beta_code_reorder():
    conv = BetaCodeReplacer(pattern=[("", "")])
    source = "*(ina/xou"
    expected = "*i(na/xou"
    output = conv.replace_beta_code(source)
    assert output == expected


def test_replace_beta_code_complete():
    conv = BetaCodeReplacer()
    source = "*(ina/xou"
    expected = "Ἱνάχου"
    output = conv.replace_beta_code(source)
    assert output == expected


def test_replace_bera_code_upper():
    conv = BetaCodeReplacer()
    source = "*(INA/XOU"
    expected = "Ἱνάχου"
    output = conv.replace_beta_code(source)
    assert output == expected
