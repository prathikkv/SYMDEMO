from src.agent import handle


def test_handle():
    assert handle({'q': 1})['status'] == 'ok'
