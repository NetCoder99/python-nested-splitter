from classes.parens_splitter import getParensCoords, splitWhenClauseLine

if __name__ == "__main__":
    #split_parens("(field1, field2)")
    #split_parens("(field1, field2, (field3, field4))")
    #split_parens("(field1, field2, (field3, field4), field5, (field6, field7))")
    #split_parens("(field1, field2, (field3, field4, (field8, field9)), field5, (field6, field7))")
    str_parts = splitWhenClauseLine("(field1, field2, (field3, field4), (field8, field9), field5, (field6, field7))")
    print(f'str_parts: {str_parts}')