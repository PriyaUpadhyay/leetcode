class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        d = defaultdict(list)
        
        def dfs(level, node):
            if not node:
                return
            d[level].append(node.val)
            
            for child in node.children:
                dfs(level+1,child)
                
        dfs(0, root)
        return d.values()
