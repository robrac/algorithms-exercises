""" 
Project: algorithms-exercises-using-python
Created by robin1885@github on 17-2-22.
"""
from pythonds.basic import Stack
from pythonds.trees import BinaryTree


def buildParseTree(fpexp):
    fplist = format_fpelist(fpexp)
    # fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parrent = pStack.pop()
            currentTree = parrent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def format_fpelist(fpexp):
    fpexp = ''.join(fpexp.split())
    fplist, num_str = [], ''
    for v in fpexp:
        if v in ['+', '-', '*', '/', '(', ')']:
            if num_str:
                fplist.append(num_str)
                num_str = ''
            fplist.append(v)
        elif v.isdecimal():
            num_str += v
    return fplist

pt = buildParseTree("((10+5)*3)")
pt.postorder()  #defined and explained in the next section
