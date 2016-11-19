import unittest

from binary_tree import BinaryTree, TreeNode


class BinaryTreeTestCase(unittest.TestCase):
    def test_BinaryTree_getroot(self):
        t = BinaryTree([1, 2])
        r = t.root()
        self.assertEqual(r.val, 1)

    def test_BinaryTree_construction(self):
        t = BinaryTree([1, 2, 3])
        r = t.root()
        self.assertEqual(r.val, 1)
        self.assertEqual(r.left.val, 2)
        self.assertEqual(r.right.val, 3)

    def test_display(self):
        t = BinaryTree([1, 2, 3])
        serialize = ' 1   \n/ \\ \n2 3 \n    \n'
        self.assertEqual(str(t), serialize)

    def test_display_big(self):
        t = BinaryTree([1, 2, 3, '#', 4, '#', 6])
        serialize = '   1       \n  / \\    \n /   \\   \n 2   3   \n  \\   \\ \n  4   6 \n        \n'
        self.assertEqual(str(t), serialize)

    def test_height(self):
        t = BinaryTree([1, 2, 3, 4, 5])
        self.assertEqual(t.height(), 3)

    def test_set_tree(self):
        t = BinaryTree([2, 3, 4])
        t2 = BinaryTree()
        t2.set_tree(t.root())
        self.assertEqual(str(t), str(t2))
