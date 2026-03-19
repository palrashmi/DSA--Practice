class Solution:
    def findCeil(self,root, x):
  
        ceil=-1
        while root:
            
            if root.data==x:
                return root.data
            elif root.data < x:
                root=root.right
            else:
                ceil=root.data
                root=root.left
        return ceil
