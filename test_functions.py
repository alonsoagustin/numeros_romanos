from functions import separate_into_units

def test_separate_into_units():
    assert separate_into_units(1) == [1]
    assert separate_into_units(11) == [10,1]
    assert separate_into_units(111) == [100,10,1]
    assert separate_into_units(1111) == [1000,100,10,1]







