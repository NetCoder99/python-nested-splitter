from typing import List

from models.parens_coords import ParensCords

def splitWhenClauseLine(inp_str: str):
    split_points = getSplitPoints(inp_str)
    str_parts    = []
    start = 0
    for index, split_point in enumerate(split_points):
        if index == 0:
            start = 0
            finis = split_point
            str_parts.append(inp_str[start:finis])
            start = finis
        else:
            finis = split_point
            str_parts.append(inp_str[start:finis])
            start = finis
    str_parts.append(inp_str[start:])
    for index, str_part in enumerate(str_parts):
        if str_part.startswith("(") and not str_part.endswith(")"):
            str_parts[index] = str_part[1:].strip()
        if str_part.endswith(")") and not str_part.startswith("("):
            str_parts[index] = str_part[:-1].strip()
        if str_part.startswith(","):
            str_parts[index] = str_part[1:].strip()
    return str_parts


def getSplitPoints(inp_str: str):
    comma_coords  = getCommaPoints(inp_str)
    parens_coords = getParensCoords(inp_str)
    inner_coords  = [paren_coord for paren_coord in parens_coords if paren_coord.nest_level == 1]
    split_points  = []
    for comma_point in comma_coords:
        is_outer = [tmp for tmp in inner_coords if tmp.close_point > comma_point > tmp.open_point ]
        if len(is_outer) == 0:
            split_points.append(comma_point)
            print(f'nest_level: {comma_point:>3} : {0}')
        else:
            print(f'nest_level: {comma_point:>3} : {is_outer[0].nest_level}')
    return split_points


def getCommaPoints(inp_str: str):
    comma_coords = []
    for index, char in enumerate(inp_str):
        if char == ",":
            comma_coords.append(index)
    print(f'comma_coords: {comma_coords}')
    return comma_coords


def getParensCoords(inp_str: str) -> List[ParensCords]:
    print(f'inp_str: {inp_str}')
    tmp_stack          = []
    parens_coords_list = []
    for index, char in enumerate(inp_str):
        if char == "(":
            tmp_stack.append(index)
        if char == ")":
            prev_coord    = tmp_stack.pop()
            parens_cords  = ParensCords(prev_coord, index)
            parens_cords.nest_level = len(tmp_stack)
            parens_coords_list.append(parens_cords)
    print(f'parens_cords: {parens_coords_list}')
    return parens_coords_list
