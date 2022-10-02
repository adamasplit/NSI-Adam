class Fraction:
    def __init__(self, num, denom):
        if denom <= 0 :
            return None
        self.num=num
        self.denom=denom