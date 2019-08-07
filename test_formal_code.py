import formal_code

# Using pytest, the following will be tested.

# To run Pytest, open terminal prompt or command prompt:

# - type: pip install pytest
# - cd into the project.
# - type: python -m pytest
# - more detailed pytest: pytest -v

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
    outcome = formal_code.convert(number=50)
    assert outcome == 'Plang'

def test_03_convert():
    outcome = formal_code.convert(number=28)
    assert outcome == 'Plong'

def test_02_convert():
    outcome = formal_code.convert(number=21)
    assert outcome == 'Pling Plong'

def test_04_convert():
    outcome = formal_code.convert(number=35)
    assert outcome == 'Plong Plang'         #-------> Test failed, it should be 'Plang Plong'

def test_05_convert():
    outcome = formal_code.convert(number=23568)
    assert outcome == 'Pling'               #-------> Test passed.

