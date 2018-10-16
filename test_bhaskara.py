import bhaskara
import pytest

class TestBhaskara:

    @pytest.fixture
    def bh(self):
        return bhaskara.Bhaskara()

    @pytest.mark.parametrize(('a, b, c, raizes'),[
    (1, 0, 0, 0),
    (1, -5, 6, (3,2)),
    (10, 10, 10, 0),
    (10, 20, 10, (-1))
    ])

    def test_bhaskara(self, bh, a, b, c, raizes):
        assert bh.calculaRaizes(a, b, c) == raizes
