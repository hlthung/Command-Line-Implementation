def from_file(filename):
        """
        :pre: filename is defined
        :post: return the array from file
        :desc: read from file and display all the value of it
        """
        a_list = List()
        infile = open(filename,'r')#read file
        #split it line by line and then read it
        contents = infile.read().splitlines()
        for i in contents:
            a_list.append(i)
        infile.close()#close infile
        return a_list
        
class List:
    """
    :pre: size is fixed with size 100 
    :post: array is changed
    """
    def __init__(self):
        """
        :pre: size, array, count are defined
        :post: None
        :desc: a constructor/ initializer
        """
        size = 100 #by default is 100
        self.array = size * [None] #initialise it with None
        self.count = 0 #Count is zero
        
    def __str__(self):
        """
        :pre: array is defined
        :post: ans is returned
        :desc: print line by line
        """
        ans = ""
        for k in range(self.count):
            #to print every element line by line
            ans = ans + str(self.array[k]) + "\n"
        return ans
           
    def __len__(self):
        """
        :pre: count is defined
        :post: count is returned
        :desc: return length
        """
        return self.count #to return the length of the array

    def __contains__(self, item):
        """
        :pre: item is defined
        :post: return True/ False
        :desc: check if array contains the item
        """
        for k in range(len(self)):
            #check every element in array with the item
            if item == self.array[k]:
                return True #return true if found
        return False #else return false if array doesn't contain the item

    def __getitem__(self, index):
        """
        :pre: index is defined
        :post: element with the index is returned
        :desc: to get item by its index
        """
        #to make the position start at 1 to n
        if index-1 < 0 or index-1 > self.count:
            #raise error
            raise IndexError("Out of range!")
        return self.array[index-1] #return the result

    def __setitem__(self, index, item):
        """
        :pre: index and item is defined
        :post: new item is set
        :desc: to set item with a specific index
        """
        #to make the position start at 1 to n
        if index-1 < 0 or index-1 > self.count:
            #raise error
            raise IndexError("Out of range!")
        self.array[index-1] = item #set new item
    
    def __eq__(self, other):
        """
        :pre: other array is defined
        :post: return False/ True
        :desc: to check if the array is same as the other array
        """
        if self.count != len(other):
            #if their length are different, return false
            return False
        else:
            #else, continue to check every element in it
            for i in range (self.count):
                #if there is one element which is not the same, return false
                if self.array[i] != other[i]:
                    return False
            return True
        
    def append(self, item):
        """
        :pre: item is defined
        :post: append array
        :desc: to append array
        """
        got_space = not self.count >= len(self.array)
        if got_space:
            self.array[self.count] = item
            self.count += 1 #increase count
        else:
            #automatic increase the size 10 times if array is full
            for i in range(self.count,self.count*10):
                self.array.append(None)
            self.array[self.count] = item
            self.count += 1 #increase count

    def insert(self, index, item):
        """
        :pre: index and item are defined
        :post: item is insert with a specific position
        :desc: to insert item BEFORE the specific position
        """
        #check range (index start with 1 to N) and it's not allowed to insert before first position
        if index-1 < 0 or index-1 > self.count:
            raise IndexError("Out of range!")
        else:
            #since index start with 1, index should be minus 2
            for i in range(self.count, index - 2, -1):
                self.array[i]= self.array[i-1]
            #insert item before index
            self.array[index-1]=item
            self.count += 1
        
    def remove(self, item):
        """
        :pre: item is defined
        :post: new array is returned
        :desc: to remove the item in array
        """
        if item not in self.array:
            #if item required not in array
            raise ValueError("Item does not exist")
        else:
            #if element in array is not the item, return it into array
            self.array = [i for i in self.array if i != item]
            self.count -= 1
            
    def delete(self, index):
        """
        :pre: index is defined
        :post: return the new array
        :desc: to delete an item with its index
        """
        #index start from 1
        valid_index = 0 <= index-1 < self.count
        if valid_index:
            #rearrange the position
            for i in range(index-1, self.count-1):
                self.array[i] = self.array[i+1]
            self.count -=1
        else:
            raise IndexError("Out of range!")
        return valid_index


      
if __name__ == "__main__":
    from_file("file.txt")
    
    


