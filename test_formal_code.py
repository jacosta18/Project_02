import formal_code

# Using pytest, the following will be tested.

def test_raindrops():
    outcome = formal_code.raindrops(number=30)
    assert outcome == ['Pling', 'Plang']

def test_convert():
    outcome = formal_code.convert(number=30)
    assert outcome == 'Pling Plang'

def test_02_convert():
    outcome = formal_code.convert(number=28)
    assert outcome == 'Plong'

def test_02_convert():
    outcome = formal_code.convert(number=28)
    assert outcome == 'Plong'

def test_03_convert():
    outcome = formal_code.convert(number=34)
    assert outcome == '34'