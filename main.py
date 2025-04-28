st = "abbcccdddd"
# a) frequency_table(st)
# Input:
frequency_table(st)
# Output:
# Character Frequencies:
# 'a': 1
# 'b': 2
# 'c': 3
# 'd': 4

'''DENNIS'''
# b) Huffman_code(st)
# Input:
Huffman_code(st)
# Output:
# Huffman Codes:
# 'a': 000
# 'b': 001
# 'c': 01
# 'd': 1

'''DENNIS'''
# c) Huffman_encode(st)
# Input:
Huffman_encode(st, codes)
# Output:
# Encoded String:
# 0000010010010101011111

# d) Huffman_tree(L)
# Input:
L = [('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')]
Huffman_tree(L)
# Output:
# (Huffman tree structure is constructed and stored in variable `tree`)

# e) Huffman_decode(bst, tree)
# Input:
bst = "0000010010010101011111"
Huffman_decode(bst, tree)
# Output:
# Decoded String:
# abbcccdddd
