from functions import separate_in_units, separate_in_thousands, small_numbers_to_roman, big_numbers_to_roman

def test_separate_in_units():
    assert separate_in_units(1) == [1]
    assert separate_in_units(11) == [10,1]
    assert separate_in_units(111) == [100,10,1]
    assert separate_in_units(1111) == [1000,100,10,1]

def test_separate_in_thousands():
    assert separate_in_thousands(3549) == [3549]
    assert separate_in_thousands(9549) == [549,9]
    assert separate_in_thousands(1000000) == [000,1000]
    assert separate_in_thousands(2363549) == [549,2363]
    assert separate_in_thousands(12363549) == [549,363,12]

def test_small_numbers_to_roman():
    assert small_numbers_to_roman([1]) == "I"
    assert small_numbers_to_roman([4]) == "IV"
    assert small_numbers_to_roman([9]) == "IX"
    assert small_numbers_to_roman([10,1]) == "XI"
    assert small_numbers_to_roman([40,4]) == "XLIV"
    assert small_numbers_to_roman([90,9]) == "XCIX"
    assert small_numbers_to_roman([100,0,0]) == "C"
    assert small_numbers_to_roman([400,0,0]) == "CD"
    assert small_numbers_to_roman([500,0,0]) == "D"
    assert small_numbers_to_roman([900,0,0]) == "CM"
    assert small_numbers_to_roman([1000,0,0,0]) == "M"
    assert small_numbers_to_roman([3000,900,90,9]) == "MMMCMXCIX"

def test_big_numbers_to_roman():
    assert big_numbers_to_roman([949,150,548,63]) == "LXIII***DXLVIII**CL*CMXLIX"
    assert big_numbers_to_roman([949,150,3548]) == "MMMDXLVIII**CL*CMXLIX"
    assert big_numbers_to_roman([549,363,12]) == "XII**CCCLXIII*DXLIX"
    assert big_numbers_to_roman([000,1000,]) == "M*"
    assert big_numbers_to_roman([949,949]) == "CMXLIX*CMXLIX"
    assert big_numbers_to_roman([949,9]) == "IX*CMXLIX"


