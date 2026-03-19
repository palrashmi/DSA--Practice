class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root
        while temp :
            if temp.val == val:
                return temp
            elif val < temp.val:
                temp=temp.left
            else:
                temp = temp.right
        return None
