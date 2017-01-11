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
    my_count = {}#Create a set first
    for word in range(1,len(a_list)+1):
        a = a_list[word]#To access the sentences per line
        for i in a.split():#To access the words per sentence  
            if i in my_count:
                my_count[i] += 1#If the word appear more than 1
            else:
                my_count[i] = 1#If the word doesnt appear before
    return my_count

def undo(a_list,stack):
    a_list = List()
    stack.pop()#To pop the last one
    #print(stack)
    a = stack.peek()#a to be the top one
    for i in a:#get the values of a
        a_list.append(i)
    return a_list

def main():
    stack = Stack()
    a_list = List()
    print("""This is a simple editor program, Please enter your option.
Or type ? to show all the function\n""")
    while True:
        choice = input('(Enter) ')#To check if user select a non-numeric option
        a = choice.split(" ")
        if len(a)== 2:
            command = str(a[0])
            value = a[1]
        elif len(a) == 3:
            command = str(a[0])
            value1 = a[1]
            value2 = a[2]
        elif len(a) == 1:
            command = str(a[0])
            value = None

        else:
            command = 'other'
            
        if command == '?':
            print("\nBasic Function")
            print("====================================================")
            print("""insert  readfile  writefile  printnum \n
        deletenum  frequency  undo  exitprogram \n""")
            print("====================================================\n")

        #Insert num
        elif command == 'insert':
            """to do insert, enter 'insert positon(space)number' to insert item. """
            try:
                temp = []#A temporary stack
                #print(a_list)
                a = value
                first = int(value1)
                second = value2
                a_list.insert(first, second)
                print(a_list)
                for i in range(1,len(a_list)+1):
                    temp.append(a_list[i])#Append all the things first, to let it becomes ['A','C']
                stack.push(temp)#Then push inside stack
                #which is what I want(can perform other operation)
                print(stack)
            except Exception:
                print("?")
           
    
        #Read filename
        elif command == 'readfile':
            """to read file, enter 'readfile your_file_name' to read in. """
            try:
                temp = []#A temporary stack
                a_list = from_file(value)
                print(a_list)
                for i in range(1,len(a_list)+1):
                    temp.append(a_list[i])#Append all the things first, to let it becomes ['A','C']
                stack.push(temp)#Then push inside stack
                #which is what I want(can perform other operation)
                print(stack)
            except Exception:
                print("?")

        #Write filename
        elif command == 'writefile':
            """to write file, enter 'writefile your_file_name' to write file. """
            try:
                write_filename(a_list,value)
            except Exception:
                print("?")
           
        #Print num
        elif command == 'printnum':
            """to print specific value, enter 'printnum index_num' to print item, no index_num means print all number """
            try:
                #value = input("Position: ")
                if value == None:#If there's no input
                    #a = None
                    print(a_list)
                else:
                    b = int(value)#Print the specific item with its position
                    print(a_list[b])
            except Exception:
                print("?")

        #Delete num
        elif command == 'deletenum':
            """to delete specific value, enter 'deletenum index_num' to delete item, no index_num means delete all number """
            try:
                temp = []#A temporary stack
                if value == None:
                    #If no position is provided
                    i = len(a_list)
                    while i > 0 :
                        a_list.delete(i)
                        i -= 1
                    print(a_list)
                    temp.append(a_list)
                    stack.push(temp)#Then push inside stack
                    #which is what I want(can perform other operation)
                    print(stack)
                else:
                    b = int(value)#Delete the specific item with its position
                    a_list.delete(b)
                    print(a_list)
                    for i in range(1,len(a_list)+1):
                        temp.append(a_list[i])#Append all the things first, to let it becomes ['A','C']
                    stack.push(temp)#Then push inside stack
                    #which is what I want(can perform other operation)
                    print(stack)
            except Exception:
                print("?")
          
        #Quit   
        elif command == 'exitprogram':
            """to exit program, enter'exitprogram'. Bye!"""
            try:
                raise SystemExit
            except Exception:
                print("?")

        #Frequency
        elif command == 'frequency':
            """to count the frequency, enter'frequency'"""
            try:
                print(frequency(a_list))
            except Exception:
                print("?")

        #Undo
        elif command == 'undo':
            """to undo the operation, enter'undo'"""
            try:
                a = undo(a_list,stack)
                print(a)
                a_list = a
                print(stack)
                #Now set a_list is the stack after operated
            except Exception:
                print("?")

        #If user choose other options        
        else:
            print('Invalid input! Try again.')
        
if __name__ == "__main__":
    main()
    
    
