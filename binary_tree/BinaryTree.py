# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        ret = '[' + str(self.val) + '] Left -> '
        if self.left:
            ret += str(self.left.val)
        else:
            ret += 'None'

        if self.right:
            ret += ' Right -> ' + str(self.right.val)
        else:
            ret += ' Right -> None'
        return ret


class BinaryTree:
    def __init__(self, serial=None):
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

    def __str__(self):
        level = self.__height
        # leading, margin
        que = [self.__root, None]
        first = True
        item_line = []
        slash_layer = int(2 ** (level - 2))
        slash_line = [[] for i in xrange(slash_layer)]
        printed = 0

        ret = ""

        while len(que) > 0 and printed <= self.__height:
            top = que[0]
            que = que[1:]
            if top is None:
                # print items
                ret += ''.join(item_line) + '\n'
                # print slash
                for line in slash_line:
                    ret += ''.join(line) + '\n'
                printed += 1
                first = True
                level -= 1
                item_line = []
                slash_layer = int(2 ** (level - 2))
                slash_line = [[] for i in xrange(slash_layer)]
                if len(que) > 0:
                    que.append(None)
                continue
            if first:
                # print leading SPACE
                item_line.append(' ' * int(2 ** (level - 1) - 1))
                for y in xrange(slash_layer):
                    slash_line[y].append(' ' * int(2 ** (level - 2) - 1))
                first = False
            if isinstance(top, TreeNode):
                item_line.append(str(top.val))
                que.append(top.left if top.left else '#')
                que.append(top.right if top.right else '#')
                for line in xrange(len(slash_line)):
                    for i in xrange(slash_layer + 1):
                        if i == slash_layer - 1 - line:
                            slash_line[line].append('/' if top.left else ' ')
                        else:
                            slash_line[line].append(' ')
                for line in xrange(len(slash_line)):
                    for i in xrange(slash_layer + int(2 ** (level - 1)) - 1):
                        if i == line:
                            slash_line[line].append('\\' if top.right else ' ')
                        else:
                            slash_line[line].append(' ')
            else:
                que.append('#')
                que.append('#')
                item_line.append(' ')
                for line in slash_line:
                    line.append(' ' * int(2 ** level))
            item_line.append(' ' * int(2 ** level - 1))
        return ret

    def display(self):
        print str(self)

    def root(self):
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

