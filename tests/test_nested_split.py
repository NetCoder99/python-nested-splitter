from classes.parens_splitter import splitNestedString

def test_simple_001():
    str_parts = splitNestedString("(field1, field2)")
    assert str_parts == ['field1', 'field2']

def test_nested_001():
    str_parts = splitNestedString("(field1, field2, (field3, field4))")
    assert str_parts == ['field1', 'field2', '(field3, field4)']

def test_nested_002():
    str_parts = splitNestedString("(field1, field2, (field3, field4), field5, (field6, field7))")
    assert str_parts == ['field1', 'field2', '(field3, field4)', 'field5', '(field6, field7)' ]

def test_nested_003():
    str_parts = splitNestedString("(field1, field2, (field3, field4, (field8, field9)), field5, (field6, field7))")
    assert str_parts == ['field1', 'field2', '(field3, field4, (field8, field9))', 'field5', '(field6, field7)' ]

def test_nested_004():
    str_parts = splitNestedString("(field1, field2,(field3, field4, (field14, field15)), (field8, field9), field5, (field6, field7, (field10, field11, (field12, field13))))")
    assert str_parts == ['field1', 'field2', '(field3, field4, (field14, field15))', '(field8, field9)', 'field5', '(field6, field7, (field10, field11, (field12, field13)))']
