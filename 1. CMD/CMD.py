import cmd
from Task import List
from Task import from_file
from stackclass import Stack

def write_filename(a_list,filename):
    outfile = open(filename,'w')
    for i in range(1,len(a_list)+1):
        outfile.write(str(a_list[i]))
        outfile.write("\n")
    outfile.close()
    return a_list

def frequency(a_list):
    my_count = {}
    for word in range(1,len(a_list)+1):
        a = a_list[word]#To access the sentences per line
        for i in a.split():#To access the words per sentence  
            if i in my_count:
                my_count[i] += 1#If the word appear more than 1
            else:
                my_count[i] = 1#If the word doesnt appear before
    return my_count

def undo(stack):
    a_list = List()
    stack.pop()
    a = stack.peek()#a to be the top one
    for i in a:#get the values of a
        a_list.append(i)
    return a_list

class TextEditor(cmd.Cmd):
    intro  = 'Welcome to simple text editor. Type help or ? to list commands.\n'
    prompt = '(Your choice)'
    a_list = List()
    stack = Stack()

    #--------basic commands-----------
    def do_insert(self, a):
        """to do insert, enter 'insert positon(space)number' to insert item. """
        try:
            temp = []
            a_list = self.array
            stack = self.stack
            ans = a.split(" ")#To seperate it by space
            first = int(ans[0])
            second = ans[1] #Input can be int or string
            a_list.insert(first,second)
            print(a_list)
            for i in range(1,len(a_list)+1):
                temp.append(a_list[i])
            stack.push(temp)
            print(stack)
            self.array = a_list
            self.stack = stack
        except Exception:
            print("?")
            
    def do_readfile(self, filename):
        """to read file, enter 'readfile your_file_name' to read in. """
        try:
            temp = []
            a_list = List()
            stack = self.stack
            a_list = from_file(filename)
            print(a_list)
            for i in range(1,len(a_list)+1):
                temp.append(a_list[i])
            stack.push(temp)
            print(stack)
            self.array = a_list
        except Exception:
            print("?")

    def do_writefile(self, filename):
        """to write file, enter 'writefile your_file_name' to write file. """
        try:
            a_list = self.array
            write_filename(a_list,filename)
            self.array = a_list
        except Exception:
            print("?")

    def do_printnum(self,position):
        """to print specific value, enter 'printnum index_num' to print item, no index_num means print all number """
        try:
            a_list = self.array
            if not position:#If there's no input
                position = None
                print(a_list)
            else:
                b = int(position)#Print the specific item with its position
                print(a_list[b])
        except Exception:
            print("?")

    def do_deletenum(self,position):
        """to delete specific value, enter 'deletenum index_num' to delete item, no index_num means delete all number """
        try:
            temp = []
            a_list = self.array
            stack = self.stack
            if not position:
                #If no position is provided
                a_list = None
                print(a_list)
                temp.append(a_list)
                stack.push(temp)
                print(stack)  
                self.array = a_list
                self.stack = stack
            else:
                b = int(position)#Delete the specific item with its position
                a_list.delete(b)
                print(a_list)
                for i in range(1,len(a_list)+1):
                    temp.append(a_list[i])
                stack.push(temp)
                print(stack)
                self.array = a_list
                self.stack = stack
        except Exception:
            print("?")

    def do_exitprogram(self,line):
        """to exit program, enter'exitprogram'. Bye!"""
        try:
            return True
        except Exception:
            print("?")
        
    def do_frequency(self, line):
        """to count the frequency, enter'frequency'"""
        try:
            a_list = self.array
            print(frequency(a_list))
        except Exception:
            print("?")
        
    def do_undo(self, line):
        """to undo the operation, enter'undo'"""
        try:
            stack = self.stack
            a = undo(stack)
            print(a)
            print(stack)
            self.array = a
        except Exception:
            print("?")
            
if __name__ == '__main__':
    TextEditor().cmdloop()
    a_list = List()
