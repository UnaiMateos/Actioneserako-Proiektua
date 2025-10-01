from main import Kalkulagailua

def test_batu_2_zenbaki():
    kalkulagailua = Kalkulagailua()
    assert kalkulagailua.batu(2, 3) == 5