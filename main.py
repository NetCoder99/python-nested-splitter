from classes.parens_splitter import *

def runTests():
    inp_str = "(field1, field2, (field3, field4, (field8, field9)), field5, (field6, field7))"
    parens_coords = getParensCoords(inp_str)
    parens_coords.sort(key=sortParensFunc)
    print(*parens_coords, sep='\n')

    str_parts = splitNestedString(inp_str)
    print(*str_parts, sep='\n')



if __name__ == "__main__":
    runTests()