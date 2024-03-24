from classes.parens_splitter import *

if __name__ == "__main__":
    #split_parens("(field1, field2)")
    #split_parens("(field1, field2, (field3, field4))")
    #split_parens("(field1, field2, (field3, field4), field5, (field6, field7))")
    #split_parens("(field1, field2, (field3, field4, (field8, field9)), field5, (field6, field7))")
    #str_parts = splitWhenClauseLine("(field1, field2, (field3, field4), (field8, field9), field5, (field6, field7))")

    inp_str = "(field1, field2, (field3, field4, (field8, field9)), field5, (field6, field7))"
    parens_coords = getParensCoords(inp_str)
    parens_coords.sort(key=sortParensFunc)
    print(*parens_coords, sep='\n')

    str_parts = splitWhenClauseLine(inp_str)
    print(*str_parts, sep='\n')

    # parens_coords = getParensCoords("(field1, field2, (field3, field4, (field14, field15)), (field8, field9), field5, (field6, field7, (field10, field11, (field12, field13))))")
    # parens_coords.sort(key=sortParensFunc)
    # print(*parens_coords, sep='\n')

    #str_parts = splitWhenClauseLine("(field1, field2,)( (field3, field4, (field14, field15)), (field8, field9), field5, (field6, field7, (field10, field11, (field12, field13))))")
    #print(*str_parts, sep='\n')

