class Range:
    """A class that mimics the built-in range class."""
    def __init__(self,start,stop=None,step=1):
        """Initialize a Range instance."""
        if step==0:
            raise ValueError("step cannot be zero")
        if stop is None:
            start,stop=0,start

        self.length=max(0,(stop-start+step-1)//step)

        self.start=start
        self.step=step

    def __len__(self):
        """Return the number of entries in the range."""
        return self.length
    
    def __getitem__(self,k):
        """Return the entry at index k (using standard interpretation if negative)."""
        if k<0:
            k+=len(self)

        if not 0<=k< self.length:
            raise IndexError("index out of range")
        
        return self.start+k*self.step
        


my_range=Range(1,10,2)

print((my_range[3]))

