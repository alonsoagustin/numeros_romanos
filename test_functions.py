from functions import separate_in_units, to_roman

def test_separate_in_units():
    assert separate_in_units(1) == [1]
    assert separate_in_units(11) == [10,1]
    assert separate_in_units(111) == [100,10,1]
    assert separate_in_units(1111) == [1000,100,10,1]

def test_to_roman():
    assert to_roman([1]) == "I"
    assert to_roman([4]) == "IV"
    assert to_roman([9]) == "IX"
    assert to_roman([10,1]) == "XI"
    assert to_roman([40,4]) == "XLIV"
    assert to_roman([90,9]) == "XCIX"
    assert to_roman([100,0,0]) == "C"
    assert to_roman([400,0,0]) == "CD"
    assert to_roman([500,0,0]) == "D"
    assert to_roman([900,0,0]) == "CM"
    assert to_roman([1000,0,0,0]) == "M"
    assert to_roman([3000,900,90,9]) == "MMMCMXCIX"