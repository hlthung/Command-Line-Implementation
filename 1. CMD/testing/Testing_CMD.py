import unittest
from Task_4 import from_file
from Task_4 import List
from Task_7 import undo
from stackclass import Stack

class Test_value(unittest.TestCase):
    """
    :pre: all the function in Task_4 are defined
    :post: to display testing result
    """
    def test_str(self):
        """
        :pre: __str__ is defined
        :post: return OK
        :desc: to test __str__ function
        """
        try:
            a_list = List()
            for i in range(5):
                a_list.append(i)
            #To test if the type of a_list is changed
            type(a_list.__str__) is a_list.__str__
            #Another way of testing
            #self.assertTrue(a_list.__str__ is not self.__str__)
        except Exception as e:
            print(e)#Try catch exception
    
    def test_len(self):
        """
        :pre: __len__ is defined
        :post: return OK
        :desc: to test __len__ function
        """
        try:
            a_list = List()
            for i in range(5):
                a_list.append(i)
            #To test the length
            self.assertEqual(len(a_list),5)#Should be 5
            self.assertNotEqual(len(a_list),4)
        except Exception as e:
            print(e)#Try catch exception

    def test_contains(self):
        """
        :pre: __contains__ is defined
        :post: return OK
        :desc: to test __contains__ function
        """
        try:
            a_list = List()
            for i in range(5):
                a_list.append(i)
            self.assertTrue(3 in a_list)
            #False as 8 is not in [0,1,2,3,4]
            self.assertFalse(8 in a_list)
        except Exception as e:
            print(e)#Try catch exception

    def test_getitem(self):
        """
        :pre: __getitem__ is defined
        :post: return OK
        :desc: to test __getitem__ function
        """
        try:
            a_list = List()
            for i in range(5):
                a_list.append(i)
            #If the first item is 0, return true
            self.assertEqual(a_list[1],0)
            #Else return false
            self.assertNotEqual(a_list[2],3)
        except Exception as e:
            print(e)#Try catch exception

    def test_setitem(self):
        """
        :pre: __setitem__ is defined
        :post: return OK
        :desc: to test __setitem__ function
        """
        try:
            a_list = List()
            for i in range(5):
                a_list.append(i)
            a_list[1]=5#Set first item is 5
            a_list[3]=9#Set third item is 9
            self.assertEqual(a_list[1], 5)
            self.assertNotEqual(a_list[3],2)#Third item should be changed
        except Exception as e:
            print(e)#Try catch exception

    def test_eq(self):
        """
        :pre: __eq__ is defined
        :post: return OK
        :desc: to test __eq__ function
        """
        try:
            a_list = List()
            for i in range(5):
                a_list.append(i)
            other1 = [0,12,3]
            other2 = [0,1,2,3,4]
            #To check if a_list is equal to other array
            self.assertTrue(a_list == other2)
            self.assertFalse(a_list == other1)
        except Exception as e:
            print(e)#Try catch exception
        
    
    def test_append(self):
        """
        :pre: append function is defined
        :post: return OK
        :desc: to test append function
        """
        try:
            a_list = List()
            for i in range(5):
                a_list.append(i)
            #Simple append checking
            self.assertEqual(len(a_list),5)
            self.assertNotEqual(len(a_list),3)
            self.assertTrue(a_list == [0,1,2,3,4])
            self.assertFalse(a_list == [0,1,2])
            #Now, we append 120 to check if it will increase the size correctly
            for j in range(120):
                a_list.append(j)
            self.assertEqual(len(a_list),125)
            self.assertNotEqual(len(a_list),100)
        except Exception as e:
            print(e)#Try catch exception
    
    def test_insert(self):
        """
        :pre: insert function is defined
        :post: return OK
        :desc: to test insert function
        """
        try:
            a_list = List()
            for i in range(5):
                a_list.append(i)
            a_list.insert(2,5)
            #Now, we need to insert 5 on position 2,
            #so it mean we need to insert it on postion 1
            self.assertTrue(a_list == [0,5,1,2,3,4])
            self.assertFalse(a_list == [0,1,2,3,4,5])
        except Exception as e:
            print(e)#Try catch exception

    def test_remove(self):
        """
        :pre: remove function is defined
        :post: return OK
        :desc: to test remove function
        """
        try:
            a_list = List()
            for i in range(5):
                a_list.append(i)
            a_list.remove(0)
            #Removed the first item
            self.assertTrue(a_list == [1,2,3,4])
            self.assertFalse(a_list == [0,1,2,3,4])     
        except Exception as e:
            print(e)#Try catch exception

    def test_delete(self):
        """
        :pre: delete function is defined
        :post: return OK
        :desc: to test delete function
        """
        try:
            a_list = List()
            for i in range(5):
                a_list.append(i)
            #To delete the first item here
            a_list.delete(1)
            self.assertTrue(a_list == [1,2,3,4])
            self.assertFalse(a_list == [0,1,2,3,4])
            #To delete the last item here
            a_list.delete(4)
            self.assertTrue(a_list == [1,2,3])
            self.assertFalse(a_list == [1,2,3,4])
        except Exception as e:
            print(e)#Try catch exception
   
    def test_fromfile(self):
        """
        :pre: from_file function is defined
        :post: return OK
        :desc: to test from_file function
        """
        try:
            a_list = from_file('file.txt')#To read a file which I prepare for testing
            #Test line by line
            self.assertEqual(a_list[1], str(5))
            self.assertEqual(a_list[2], str(6))
            self.assertEqual(a_list[3], str(7))
            self.assertEqual(a_list[4], str(8))
            self.assertEqual(a_list[5], str(9))
            #To check length
            self.assertEqual(len(a_list), 5)
            #An example that is false
            #self.assertNotEqual(a_list[5], str(6))  
        except Exception as e:
            print(e)#Try catch exception

    def test_undo(self):
        """
        :pre: from_file function is defined
        :post: return OK
        :desc: to test from_file function
        """
        try:
            stack = Stack()
            a_list = from_file('file.txt')
            #a_list becomes [5,6,7,8,9]
            temp1 = []
            for i in range(1,len(a_list)+1):
                temp1.append(a_list[i])
            stack.push(temp1)
            a_list.insert(2,str(3))
            #a_list becomes [5,3,6,7,8,9]
            temp2 = []
            for i in range(1,len(a_list)+1):
                temp2.append(a_list[i])
            stack.push(temp2)
            a_list.delete(3)
            #a_list becomes [5,3,7,8,9]
            temp3 = []
            for i in range(1,len(a_list)+1):
                temp3.append(a_list[i])
            stack.push(temp3)
            a = undo(stack)
            self.assertEqual(a[1], str(5))
            self.assertEqual(a[2], str(3))
            self.assertEqual(a[3], str(6))
            self.assertEqual(a[4], str(7))
            self.assertEqual(a[5], str(8))
            self.assertEqual(a[6], str(9))
            #To check length
            self.assertEqual(len(a), 6)
        except Exception as e:
            print(e)#Try catch exception
    
if __name__ == '__main__':
    unittest.main()
