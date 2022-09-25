#Time Complexity:: hashkey(): O(1), doublhashkey(): O(1), add(): O(n) at times, remove(): O(1), contains(): , Average: Moving towards O(1)
#Space Complexity:: O(n) where n is the maximum number of elements
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No


class MyHashSet(object):

    def __init__(self):
        self.length = 1000 #setting the length of the primary array to 10^3 since 10^6 is max no. of keys
        self.primary=[None]*self.length #initializing hashset
    
    def hashkey(self,key): 
        return key%self.length #hashkey of the first 1000 keys
    
    def doublehashkey(self,key):
        return key//self.length #hashkey of keys larger than 1000
        
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_index = self.hashkey(key) #assigning the hashkey to a variable
        double_hash_index = self.doublehashkey(key) #assigning the hashkey to a variable
        
        if self.primary[hash_index]==None: #checks if hashindex already has a secondary DS
            if hash_index == 0:
                self.primary[hash_index] = [False]*(self.length + 1) #create a DS to store zero aswell
            else:
                self.primary[hash_index] = [False]*self.length #
        
        self.primary[hash_index][double_hash_index] = True
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_index = self.hashkey(key)
        double_hash_index = self.doublehashkey(key)
        
        if self.primary[hash_index]!=None:
            self.primary[hash_index][double_hash_index] = False
        
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hash_index = self.hashkey(key)
        double_hash_index = self.doublehashkey(key)
        
        if self.primary[hash_index]!=None:
            return self.primary[hash_index][double_hash_index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)