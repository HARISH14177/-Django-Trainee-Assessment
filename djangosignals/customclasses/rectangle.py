class Rectangle:
    def __init__(self, length: int, width: int):
        """
        Initialize a Rectangle with length and width.
        
        Args:
            length: The length of the rectangle (int)
            width: The width of the rectangle (int)
        """
        self.length = length
        self.width = width
    
    def __iter__(self):
        """
        Make Rectangle iterable.
        Returns an iterator that yields length and width as dictionaries.
        """
        # Create a list of values to iterate over
        self._values = [
            {'length': self.length},
            {'width': self.width}
        ]
        self._index = 0
        return self
    
    def __next__(self):
        """
        Return the next value when iterating.
        Raises StopIteration when all values have been returned.
        """
        if self._index < len(self._values):
            value = self._values[self._index]
            self._index += 1
            return value
        else:
            # End of iteration
            raise StopIteration


# Example usage:
if __name__ == "__main__":
    # Create a rectangle
    rect = Rectangle(10, 5)
    
    # Iterate over it
    for item in rect:
        print(item)
    
    # Output will be:
    # {'length': 10}
    # {'width': 5}