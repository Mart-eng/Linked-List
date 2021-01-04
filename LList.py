from ListNode import ListNode

class LList:

    #------------------------------------------------------------

    def __init__(self, seq=()):

        """create an LList
        pre: seq is a list
        post: creates a list containing items in seq"""
     
        if seq == ():
            # No items to put in, create an empty list
            self.head = None
        else:
            # Create a node for the first item
            self.head = ListNode(seq[0], None)

            # Add remaining items keeping track of last node added
            last = self.head
            for item in seq[1:]:
                last.link = ListNode(item, None)
                last = last.link
                
        self.last = last
        self.size = len(seq)
   
    #------------------------------------------------------------

    def __len__(self):

        '''post: returns number of items in the list'''

        return self.size

    #------------------------------------------------------------

    def _find(self, position):

        '''private method that returns node that is at location position
        in the list (0 is first item, size-1 is last item)
        pre: 0 <= position < self.size
        post: returns the ListNode at the specified position in the
        list'''
        
        assert 0 <= position < self.size

        node = self.head
        # move forward until we reach the specified node
        for i in range(position):
            
                
            node = node.link
        return node

    #------------------------------------------------------------

    def append(self, x):

        '''appends x onto end of the list 
        post: x is appended onto the end of the list'''

        #self.last makes this operation theta(1)
        newNode = ListNode(x,None)
        if self.head is not None:
            self.last.link = newNode
            
        else:
            self.head = newNode
            
        self.last = newNode     
        self.size += 1 

##        # create a new node containing x
##        newNode = ListNode(x)
##
##        # link it into the end of the list
##        if self.head is not None:
##            # non-empty list
##            node = self._find(self.size - 1)
##            node.link = newNode
##        else:
##            # empty list
##            # set self.head to new node
##            self.head = newNode
        
    
    #------------------------------------------------------------

    def __getitem__(self, position):

        '''return data item at location position
        pre: 0 <= position < size
        post: returns data item at the specified position'''

        node = self._find(position)
        return node.item
    
    #------------------------------------------------------------

    def __setitem__(self, position, value):

        '''set data item at location position to value
        pre: 0 <= position < self.size
        post: sets the data item at the specified position to value'''

        node = self._find(position)
        node.item = value

    #------------------------------------------------------------

    def __delitem__(self, position):

        '''delete item at location position from the list
        pre: 0 <= position < self.size
        post: the item at the specified position is removed from 
        the list'''

        assert 0 <= position < self.size

        self._delete(position)
        self.size -= 1

    #------------------------------------------------------------

    def _delete(self, position):

        #private method to delete item at location position from the list
        # pre: 0 <= position < self.size
        # post: the item at the specified position is removed from the list
        # and the item is returned (for use with pop)

        if position == 0:
            # save item from the initial node
            item = self.head.item

            # change self.head to point "over" the deleted node
            self.head = self.head.link

        #elif position == self.size - 1:
            
            
            #prev_node = self._find(position - 1)
           # prev_node.link = None
           
        else:

            
            # find the node immediately before the one to delete
            prev_node = self._find(position - 1)

            # save the item from node to delete
            item = prev_node.link.item

            # change predecessor to point "over" the deleted node
            prev_node.link = prev_node.link.link

        self.size -= 1
        
        return item

    #------------------------------------------------------------

    def pop(self, i=None):

        '''returns and removes at position i from list; the default is to
        return and remove the last item

        pre: self.size > 0 and ((i is None or (0 <= i < self.size))

        post: if i is None, the last item in the list is removed
        and returned; otherwise the item at position i is removed 
        and returned'''

        assert self.size > 0 and (i is None or (0 <= i < self.size))

        # default is to delete last item
        # i could be zero so need to compare to None
        if i is None:
            i = self.size - 1
            self.last = self.size - 2
            
        self.last = self.size - 1
        return self._delete(i)

    #------------------------------------------------------------

    def insert(self, i, x):

        '''inserts x at position i in the list
        pre: 0 <= i <= self.size
        post: x is inserted into the list at position i and 
              old elements from position i..oldsize-1 are at positions 
              i+1..newsize-1'''

        assert 0 <= i <= self.size

        if i == 0:
            # insert before position 0 requires updating self.head
            self.head = ListNode(x, self.head)

        
        else:
            # find item that node is to be insert after
            node = self._find(i - 1)
            node.link = ListNode(x, node.link)

            if i == self.size:
                self.last = node.link

        
        self.size += 1

    #------------------------------------------------------------

    def __copy__(self):
    
        '''post: returns a new LList object that is a shallow copy of self'''
        
        a = LList()
        node = self.head
        while node is not None:
            a.append(node.item)
            node = node.link
        return a

    #-------------------------------------------------------------

    def __max__(self):

        '''post: returns the highest value in the linked list'''
        
        if self.head == None:
            return None

        node = self.head
        largest = node.item
        while node != None:
            if node.item > largest:
                largest = node.item
            node = node.link
            
        return largest

    #-------------------------------------------------------------

    def __min__(self):
        
        '''post: returns the smallest value in the linked list'''
        if self.head == None:
            return None

        node = self.head
        smallest = node.item
        while node != None:
            if node.item < smallest:
                smallest = node.item
            node = node.link
            
        return smallest
    #-------------------------------------------------------------

    def index(self,position):
        
        ''' returns the value at the position
            pre: 0<= position <= len(llist) - 1
            post: return value of the node'''

        node = self.head
        for i in range(position):
            node = node.link
            
        return node.item

    #------------------------------------------------------------

    def count(self,x):

        ''' count how many values x appears in the list'''
        
        node = self.head
        count = 0
        for i in range(self.size):
            if node.item == x:
                count += 1
            node = node.link
            
        return count

    #------------------------------------------------------------

    def remove(self,x):

        ''' removes the first occurance of x from the list'''
        
  ####currently works for every position but the last
        
        node = self.head
        while node.item != x:

            if node.item == None:
                break
            
            node = node.link

            
             
        if node.item == x:
            #self.__delitem__(x)
            self._delete(x)
            self.size -= 1

        
            
       
      
            

    #------------------------------------------------------------
        
               
            
    def __iter__(self):

        # generator version works in both Python2 and Python3
         node = self.head
         while node is not None:
             yield node.item
             node = node.link

   #----------ADDED BY NN -----------------------------------------

    def __str__(self):
        """ post: displays the elements of the list """
        
        l = [self.head.item] # add the first element of LList to list of values
        nxt = self.head
        
        for i in range(1,self.size):
            nxt = nxt.link
            l.append(nxt.item)
            
        return str(l)
             

    #------------------------------------------------------------

##    def __iter__(self):
##
##        return LListIterator(self.head)

#------------------------------------------------------------

##class LListIterator:
##
##    #------------------------------------------------------------
##
##    def __init__(self, head):
##        self.currnode = head
##
##    #------------------------------------------------------------
##    # Python2 version
##    def next(self):
##        if self.currnode is None:
##            raise StopIteration
##        else:
##            item = self.currnode.item
##            self.currnode = self.currnode.link
##            return item
##
##    #------------------------------------------------------------
##    # Python3 version
##    def __next__(self):
##        if self.currnode is None:
##            raise StopIteration
##        else:
##            item = self.currnode.item
##            self.currnode = self.currnode.link
##            return item



#------------- Testing ----------------------
print()
L = LList([5,1,2,3,4,0,1])
print("Here is our LList:",L)
#print(min(L))
print("The smallest value is ",L.__min__())
print("The largest value is ",L.__max__())
print("index of value 3 is ",L.index(3))
print("index of value 5 is ",L.index(5))
print("index of value 0 is ",L.index(0))
#print("index of value 7 is ",L.index(7))
print("There are",L.count(1),"ones in the list")

print("\n Deleting 3 from the list ... ")
L.remove(3)
print(L)
print("should be: [5,1,2,4,0,1]")

print("Trying to delete an non-existing value of 10 from the list...")
L.remove(10)

print("\n The tail node before appending 7:",L.last.item)
print("After appending 7:")
L.append(7)
print(L)
print("The tail's value:",L.last.item)

print("\n Deleting 7 from the list...")
L.pop()
print(L)
print("The tail's value:",L.last.item)

print("\n Appending 12...")
L.append(12)
print(L)
print("The tail's value:",L.last.item)

print("\n Inserting a value 23 at the end...")
L.insert(len(L),23)
print(L)
print("The tail's value:",L.last.item)

print("\ndeleting the last value from the list using __delitem__ method ...")
L.__delitem__(7)
print(L)
print("The tail's value:",L.last.item)

