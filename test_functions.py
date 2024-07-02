from functions import separate_into_units, to_roman

def test_separate_into_units():
    assert separate_into_units(1) == [1]
    assert separate_into_units(11) == [10,1]
    assert separate_into_units(111) == [100,10,1]
    assert separate_into_units(1111) == [1000,100,10,1]

def test_to_roman():
    assert to_roman(1) == "I"
    assert to_roman(2) == "II"
    assert to_roman(3) == "III"

    assert to_roman(4) == "IV"

    assert to_roman(5) == "V"
    assert to_roman(6) == "VI"
    assert to_roman(7) == "VII"
    assert to_roman(8) == "VIII"

    assert to_roman(9) == "IX"
    assert to_roman(10) == "X"





