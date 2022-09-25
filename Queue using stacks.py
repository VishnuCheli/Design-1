#Time Complexity:: push(): O(1), pop(): O(1), peek(): O(n) at times, empty(): O(1) Average: Moving towards O(1)
#Space Complexity:: O(n) where n is the maximum number of elements
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class MyQueue(object):

    def __init__(self): 
        self.instack = [] #creating first array to use as a pushing stack
        self.outstack = [] #creating second array to use as a popping stack
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.instack.append(x) #pushes all incoming elements into the instack

    def pop(self):
        """
        :rtype: int
        """
        if len(self.outstack)!=0: #ensures outstack isn't empty before popping element
            return self.outstack[-1] #returns first element from queue
        self.out[-1]== 0 #removes first element in the queue
                             
    def peek(self):
        """
        :rtype: int
        """
        if len(self.outstack)== 0: #checks if outstack is empty
            while self.instack: #this loop pushes all elements from instack to outstack
                val = self.instack.pop()
                self.outstack.append(val)
                             
        return self.outstack[-1] #returns first element of the queue
        

    def empty(self):
        """
        :rtype: bool
        """
        if(self.outstack[0]==0): #checks if queue is emepty
            return True
        else:
            return False