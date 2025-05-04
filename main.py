'''Matthew'''
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

'''Matthew'''
# Pops top element from a minheap, then sorts it
def pop_minheap(heap):
    if (len(heap) == 0):
        return
    if (len(heap) == 1):
        return heap.pop()
    popped = heap[0]

    heap[0] = heap.pop()
    i = 0
    # Sorting starts
    while True:
        s = i
        if ((i * 2 + 1) < len(heap) and heap[i * 2 + 1][1] < heap[s][1]):
            s = i * 2 + 1
        if ((i * 2 + 2) < len(heap) and heap[i * 2 + 2][1] < heap[s][1]):
            s = i * 2 + 2
        if s != i:
            heap[s], heap[i] = heap[i], heap[s]
            i = s
        else:
            break
        
    return popped

'''Matthew'''
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

'''Yonghyeon'''
# d) Huffman_tree(L)
# Input:
def Huffman_tree(L):
    root = {}
    for char, code in L:
        node = root
        for bit in code:
            if bit not in node:
                node[bit] = {}
            node = node[bit]
        node['char'] = char 
    return root

# Output:
# (Huffman tree structure is constructed and stored in variable `tree`)

'''Yonghyeon'''
# e) Huffman_decode(bst, tree)
# Input:
def Huffman_decode(bst, tree):
    result = ''
    node = tree
    for bit in bst:
        node = node[bit]
        if 'char' in node:
            result += node['char']
            node = tree  # 다시 루트로 리셋
    print("Decoded String:")
    print(result)
# Output:
# Decoded String:
# abbcccdddd

#Given examples:
#L = [('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')]
st = "This is a test. This is only a test."
#bst = "0000010010010101011111"

x = into_minheap(frequency_table(st))

print(x)
for i in range(len(x)):
    print(pop_minheap(x))