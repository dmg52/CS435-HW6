# a) frequency_table(st)
# Input:
def frequency_table(st):
    table = {}
    for i in st:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1
    for i in table.items():
        print(i[0] + ": " + str(i[1]))
    return
# Output:
# Character Frequencies:
# 'a': 1
# 'b': 2
# 'c': 3
# 'd': 4

'''DENNIS'''
# b) Huffman_code(st)
# Input:
def Huffman_code(st):
    return
# Output:
# Huffman Codes:
# 'a': 000
# 'b': 001
# 'c': 01
# 'd': 1

'''DENNIS'''
# c) Huffman_encode(st)
# Input:
def Huffman_encode(st, codes):
    return
# Output:
# Encoded String:
# 0000010010010101011111

# d) Huffman_tree(L)
# Input:
def Huffman_tree(L):
    return
# Output:
# (Huffman tree structure is constructed and stored in variable `tree`)

# e) Huffman_decode(bst, tree)
# Input:
def Huffman_decode(bst, tree):
    return
# Output:
# Decoded String:
# abbcccdddd

#Given examples:
#L = [('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')]
st = "abbcccdddd"
#bst = "0000010010010101011111"

frequency_table(st)