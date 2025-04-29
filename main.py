# MinHeap constructor function, takes a dictionary of letters and their frequencies
def into_minheap(dict):
    heap = []
    for i in dict.items():
        heap.append(i)
        # index of new element
        i = len(heap) - 1
        while i > 0 and heap[(i - 1) // 2][1] > heap[i][1]:
            heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
            i = (i - 1) // 2
    return heap

# Pops top element from a minheap
def pop_minheap(heap):
    return

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
    return table
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

x = into_minheap(frequency_table(st))
for i in x:
    print(i)