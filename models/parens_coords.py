class ParensCords:
    open_point:   int
    close_point:  int
    nest_level:   int
    def __init__(self, open_point:int, close_point:int):
        self.open_point  = open_point
        self.close_point  = close_point
        self.nest_level   = -1
    def __repr__(self):
        return f'[{self.open_point:>3}:{self.close_point:>3}] :: {self.nest_level}'