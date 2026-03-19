class Solution:
  def minValue(self,root):
    if root is None:
      return None
    while root and root.left:
      root=root.left
    return root.val
