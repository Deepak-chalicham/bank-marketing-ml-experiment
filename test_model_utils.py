from model_utils import convert_target


def test_convert_yes():
    assert convert_target("yes") == 1


def test_convert_no():
    assert convert_target("no") == 0