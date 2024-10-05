from classes.parens_splitter import *

# -----------------------------------------------------------------
# test command :: python -m pytest -v --tb=line
# -----------------------------------------------------------------

def runTests():
    inp_str = "(field1 == 2, field2 in (1, 2, 3), (field3 == field4 - 1, field4, (field8, field9)), field5, (field6, field7))"
    parens_coords = getParensCoords(inp_str)
    parens_coords.sort(key=sortParensFunc)
    print(*parens_coords, sep='\n')

    str_parts = splitNestedString(inp_str)
    print(inp_str)
    for str_part in str_parts:
        print(f'-{str_part}')
        if ',' in str_part:
            str_parts2 = splitNestedString(str_part)
            print(f'--{str_parts2}', sep='\n')


#    print(*str_parts, sep='\n')



if __name__ == "__main__":
    runTests()