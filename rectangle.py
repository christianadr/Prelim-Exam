class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (2*self.length) + (2*self.width)
    
if __name__ == '__main__':
    rect = Rectangle(5, 10)
    print(rect.perimeter())