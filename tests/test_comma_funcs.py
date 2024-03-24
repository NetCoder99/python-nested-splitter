from classes.parens_splitter import getCommaPoints

def test_comma_001():
    str_parts = getCommaPoints("(field1, field2)")
    assert str_parts == [8]

def test_comma_002():
    str_parts = getCommaPoints("(field1, field2, (field3, field4))")
    assert str_parts == [7, 15, 24]
