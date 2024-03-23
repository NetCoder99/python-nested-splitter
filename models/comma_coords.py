class CommaCords:
    comma_index:   int
    nest_level:   int
    def __init__(self, comma_index:int):
        self.comma_index  = comma_index
        self.nest_level   = -1
    def __repr__(self):
        return f'[{self.comma_index:>3}] :: {self.nest_level}'