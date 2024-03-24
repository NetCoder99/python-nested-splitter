from typing import List

from classes.parens_splitter import getParensCoords
from models.parens_coords import ParensCords


def test_parens_001():
    str_parts:List[ParensCords] = getParensCoords("(field1, field2)")
    assert len(str_parts) == 1
    assert str_parts[0].open_point == 0
    assert str_parts[0].close_point == 14
    assert str_parts[0].nest_level == 0

