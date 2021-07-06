class Slice:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def len(self):
        return self.right - self.left

    def med(self):
        return (self.right + self.left) / 2
