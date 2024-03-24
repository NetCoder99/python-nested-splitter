from typing import List

from models.parens_coords import ParensCords

# -----------------------------------------------------------------------------
# Splitting a string on the commas, when those commas are nested within a set
# of nested parentheses can be tricky.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# consider the following: "(field1, field2, (field3, field4))"
# the basic theory is to build a 'stack' like object to manage the 'nested'
# level of the split delimiter.
# Scan from left to right, when you hit an opening '(' push that index onto
# the stack, when you hit a closing ')' simply pop that last opening '(' and
# you will have matched the opening and closing parentheses with the added
# bonus that the depth, or length, of the opening paren stack will reflect
# how deeply nested the parentheses set is.
# -----------------------------------------------------------------------------
def splitWhenClauseLine(inp_str: str):
    print(inp_str)
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
        str_parts[index] = trimInpString(str_part)
    return str_parts

# -----------------------------------------------------------------------------
# trim / clean the unwanted characters from start and stop of string
# -----------------------------------------------------------------------------
def trimInpString(inp_str: str):
    str_temp = inp_str
    if str_temp.startswith(","):
        str_temp = str_temp[1:].strip()

    if str_temp.startswith("(") and not str_temp.endswith(")"):
        str_temp = str_temp[1:].strip()

    if str_temp.endswith(")"):
        open_count = str_temp.count('(')
        clse_count = str_temp.count(')')
        if clse_count > open_count:
            # remove count of opening parens
            str_temp = str_temp[:open_count - clse_count].strip()
    return str_temp


# -----------------------------------------------------------------------------
# scan the parentheses indexes and fetch the nested level of the comma's
# -----------------------------------------------------------------------------
def getSplitPoints(inp_str: str):
    comma_coords  = getCommaPoints(inp_str)
    parens_coords = getParensCoords(inp_str)
    inner_coords  = [paren_coord for paren_coord in parens_coords if paren_coord.nest_level == 1]
    split_points  = []
    for comma_point in comma_coords:
        is_outer = [tmp for tmp in inner_coords if tmp.close_point > comma_point > tmp.open_point ]
        if len(is_outer) == 0:
            split_points.append(comma_point)
    return split_points


# -----------------------------------------------------------------------------
# fetch the in-string indexes of all commas within the input string
# -----------------------------------------------------------------------------
def getCommaPoints(inp_str: str):
    comma_coords = []
    for index, char in enumerate(inp_str):
        if char == ",":
            comma_coords.append(index)
    return comma_coords


# -----------------------------------------------------------------------------
# create a list of the in-string points of the opening and closing parentheses
# -----------------------------------------------------------------------------
def getParensCoords(inp_str: str) -> List[ParensCords]:
    tmp_stack          = []
    parens_coords_list = []
    for index, char in enumerate(inp_str):
        if char == "(":
            tmp_stack.append(index)
        if char == ")":
            try:
                prev_coord    = tmp_stack.pop()
                parens_cords  = ParensCords(prev_coord, index)
                parens_cords.nest_level = len(tmp_stack)
                parens_coords_list.append(parens_cords)
            except Exception:
                raise Exception('Unbalanced closing parentheses detected!')

    if len(tmp_stack) > 0:
        raise Exception('Unbalanced opening parentheses detected!')

    return parens_coords_list

def sortParensCoords(parens_coords: List[ParensCords]):
    return parens_coords.sort(key=sortParensFunc)

def sortParensFunc(parens_coord: ParensCords):
    return parens_coord.open_point
