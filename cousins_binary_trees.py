class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root: 
            return False
        
        queue = deque([(root, None)]) 

        while queue:
            level_size = len(queue)
            x_parent = y_parent = None

            for _ in range(level_size): 
                node, parent = queue.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
           
            if x_parent and y_parent:
                return x_parent != y_parent 
            if x_parent or y_parent:
                return False 
        return False  
    
# Time complexity - O(n)
# Space complexity - O(n)