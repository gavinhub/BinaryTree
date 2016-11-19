import unittest

from binary_tree import TreeNode


class TreeNodeTestCase(unittest.TestCase):
    def test_TreeNode(self):
        n = TreeNode(3)
        self.assertEqual(n.val, 3)
        self.assertEqual(n.left, None)

    def test_TreeNode_str(self):
        n = TreeNode(4)
        n2 = TreeNode(5)
        n.left = n2
        x = str(n)
        self.assertEqual(x, '[4] Left -> 5 Right -> None')
