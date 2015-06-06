# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x = None):
		self.val = x
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self, serial = None):
		self.__size = 0
		self.__root = None
		self.__height = 0
		if serial:
			if isinstance(serial, list):
				self.construct(serial)
			elif isinstance(serial, TreeNode):
				self.set_tree(serial)

	# serial should be a list
	def construct(self, serial):
		self.__root = TreeNode(serial[0])
		self.__height = 1
		self.__size = 1
		que = [[self.__root, 0], [None, 0]]
		newLevel = True
		i = 1
		while i < len(serial):
			top = que[0]
			if newLevel:
				self.__height += 1
				newLevel = False
			if top[0] is None:
				# change level
				newLevel = True
				que = que[1:]
				que.append([None, 0])
				continue
			else:
				# left node
				if top[1] == 0:
					top[1] = 1
					if serial[i] != '#':
						top[0].left = TreeNode(serial[i])
						que.append([top[0].left, 0])
						self.__size += 1
				# right node
				else:
					que = que[1:]
					if serial[i] != '#':
						top[0].right = TreeNode(serial[i])
						que.append([top[0].right, 0])
						self.__size += 1
				i += 1



	def display(self):
		level = self.__height
		#leading, margin
		que = [self.__root, None]
		first = True
		itemLine =[]
		slashLayer = int(2**(level-2))
		slashLine = [[] for i in xrange(slashLayer)]
		printed = 0
		while(len(que) > 0 and printed <= self.__height):
			top = que[0]
			que = que[1:]
			if top is None:
				# print items
				print ''.join(itemLine)
				# print slash
				for line in slashLine:
					print ''.join(line)
				printed += 1
				first = True
				level -= 1
				itemLine = []
				slashLayer = int(2**(level-2))
				slashLine = [[] for i in xrange(slashLayer)]
				if len(que) > 0:
					que.append(None)
				continue
			if first:
				# print leading SPACEs
				itemLine.append(' ' * int(2**(level-1)-1))
				for y in xrange(slashLayer):
					slashLine[y].append(' ' * int(2**(level-2)-1))
				first = False
			if isinstance(top, TreeNode):
				itemLine.append(str(top.val))
				que.append(top.left if top.left else '#')
				que.append(top.right if top.right else '#')
				for line in xrange(len(slashLine)):
					for i in xrange(slashLayer+1):
						if i == slashLayer-1-line:
							slashLine[line].append('/' if top.left else ' ')
						else:
							slashLine[line].append(' ')
				for line in xrange(len(slashLine)):
					for i in xrange(slashLayer + int(2**(level-1)) -1):
						if i == line:
							slashLine[line].append('\\' if top.right else ' ')
						else:
							slashLine[line].append(' ')
			else:
				que.append('#')
				que.append('#')
				itemLine.append(' ')
				for line in slashLine:
					line.append(' ' * int(2**level))
			itemLine.append(' ' * int(2**level-1))
			
	def tree(self):
		return self.__root

    def height(self):
        return self.__height

	def set_tree(self, root):
		self.__root = root
		self.__height = 1
		self.__size = 0
		que = [root, None]
		while len(que) > 1:
			top = que.pop(0)
			if top is None:
				que.append(None)
				self.__height += 1
			else:
				self.__size += 1
				if top.left:
					que.append(top.left)
				if top.right:
					que.append(top.right)




if __name__ == '__main__':
	tree = BinaryTree([1,2,3,4,5,'#',6,7,'#','#','#','#',8])
	tree.display()
	z = BinaryTree(tree.tree())
	z.display()
