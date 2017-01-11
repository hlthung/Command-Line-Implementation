class Stack:
    """
    :pre: size is fixed with size 100 
    """
    def __init__(self):
        """
        :pre: size, array, count are defined
        :post: None
        :desc: a constructor/ initializer
        """
        size = 100#by default is 100
        self.stack = 100 * [None]
        self.count = 0#count is zero
        self.top = -1

    def __str__(self):
        """
        :pre: array is defined
        :post: display is returned
        :desc: print stack
        """
        display="Stack is: \n"
        pos = self.top #start from the top 
        while pos>=0:
            display = display + str(self.stack[pos])+"\n"
            pos-=1
        return display

    def is_empty(self):
        """
        :desc: is empty when count = 0
        """
        return self.count == 0

    def is_full(self):
        """
        :desc: is full when count = len(array)
        """
        return self.count == len(self.stack)

    def size(self):
        """
        :desc: return size
        """
        return self.count

    def push(self, item):
        """
        :pre: item is defined
        :desc: to push item inside
        """
        assert not self.is_full(), "Full!"
        self.stack[self.count] = item
        self.count += 1#count add 1
        self.top += 1#top add 1

    def pop(self):
        """
        :pre: None
        :post: item is returned
        :desc: to pop item out
        """
        assert not self.is_empty(), "Empty!"
        item = self.stack[self.top]
        self.top -= 1#top minus 1
        self.count -= 1#count minus 1
        return item

    def peek(self):
        """
        :pre: None
        :post: array[top] is returned
        :desc: get value of the top
        """
        assert not self.is_empty(), "Empty!"
        return self.stack[self.top]

    def reset(self):
        """
        :desc: to reset
        """
        self.count = 0
        self.top = -1
