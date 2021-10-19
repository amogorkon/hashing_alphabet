import use

from hashlib import sha256
jh = use(use.Path("../src/jackhash/jackhash.py"))


def test_alphabet():
    H = sha256("hello world".encode("utf-8")).hexdigest()
    assert H == jh.num_as_hexdigest(jh.JACK_as_num(jh.hexdigest_as_JACK(H)))
