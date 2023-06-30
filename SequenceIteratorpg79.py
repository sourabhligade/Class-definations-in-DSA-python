class SequenceIterator:
    """An iterator for Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self.seq = sequence
        self.k = -1

    def __next__(self):
        """Return the next element, or raise StopIteration error."""
        self.k += 1
        if self.k < len(self.seq):
            return self.seq[self.k]
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


sequence = [1, 2, 3, 4, 5]
iterator = SequenceIterator(sequence)

for element in iterator:
    print(element)
