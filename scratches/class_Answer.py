

class QuadAnswer:
    def __init__(self, error_type, x1 = 0, x2 = 0, str = ''):
        self.type = error_type
        self.x1 = x1
        self.x2 = x2
        self.str = str

    def __str__(self) -> str:
        if self.type == TYPE_TWO_ROOTS:
            return 'x1 = {}\n x2 = {}\n'.format(self.x1, self.x2)
        if self.type == TYPE_ONE_ROOT:
            return 'x = {}\n'.format(self.x1)
        if self.type == TYPE_ERROR:
            raise Exception(self.str)
        if self.type == TYPE_NO_ROOTS:
            return 'No Roots \n'.format(self.str)
        if self.type == TYPE_ANY_ROOT:
            return 'Any Root \n'.format(self.str)
        