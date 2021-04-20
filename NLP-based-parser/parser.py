from lark import Lark

l = Lark.open("Grammar.lark")


sentence = input()
tree = l.parse(sentence)
print(tree)
print(tree.pretty("   "))
