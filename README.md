BinaryTree for LeetCode
==============
***BinaryTree.py*** is a handy tool which can **construct** and **display** the binary trees you need when coding for [LeetCode](https://oj.leetcode.com/)

DEMO
------------
1. You need to import the class before using it
	
		import BinaryTree as bt
	
1. Construct a binary tree from a list of values/objects or a binary tree

		t1 = bt.BinaryTree([1,2,3,4,5,'#',6,7,'#','#','#','#',8])
		t2 = bt.BinaryTree(t1.root())
        node = bt.TreeNode(4)

1. Get the root of the binary tree

		r = t.root()
		print r 
		# Out: [4] Left -> None Right -> None

1. Display the tree

		t.display()

	And you get:
		

		       1               
		      / \          
		     /   \         
		    /     \        
		   /       \       
		   2       3       
		  / \       \    
		 /   \       \   
		 4   5       6   
		/             \ 
		7             8 

		
1. Test
	
	    python -m unittest -v test


LeetCode Binary Tree Serialization
-----------------
See [LeetCode](https://oj.leetcode.com/problems/binary-tree-level-order-traversal/), click "read more on how binary tree is serialized on OJ"
