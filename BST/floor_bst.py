class Solution:
    def findFloor(self, root, x):
      
        floor=-1
        temp=root
        while temp:
            if x >= temp.data:
                floor=temp.data
                temp=temp.right
                
            else:
                temp=temp.left
        return floor
