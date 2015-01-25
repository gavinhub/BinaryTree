BinaryTree for LeetCode
==============
***BinaryTree.py*** is a handy tool which can **construct** and **display** the binary trees you need when coding for [LeetCode](https://oj.leetcode.com/)

DEMO
------------
1. You need to import the class before using it
	
		from BinaryTree import *
	
1. Construct a binary tree with a list of values/objects

		t = BinaryTree([1,2,3,4,5,'#',6,7,'#','#','#','#',8])

1. Get the root of the binary tree

		r = t.tree()

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

		
LeetCode Binary Tree Serialization
-----------------
See [LeetCode](https://oj.leetcode.com/problems/binary-tree-level-order-traversal/), click "read more on how binary tree is serialized on OJ"
