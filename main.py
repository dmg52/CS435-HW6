# Dennis Gannon dmg52, Yonghyeon Shin ys97, Matthew Tohon mdt26
# CS 435 - Homework 6

'''Matthew'''
# MinHeap constructor function, takes a dictionary of letters and their frequencies
def into_minheap(dict):
    heap = []
    for i in dict.items():
        heap.append(i)
        sort_minheap(heap)

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

'''Dennis'''
# Insert into heap with (char, freq) node
def insert_minheap(heap, node):
    heap.append(node)
    sort_minheap(heap)

'''Dennis'''
def sort_minheap(heap):
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[i][1] < heap[parent][1]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

'''Dennis'''
# Create Huffman Codes for heap and returns final coded tree
# Code prefix sent to child
def heap_codes(heap, code_prefix = "", codes = None):
    if codes is None:
        codes = {}

    if not isinstance(heap, tuple):
        codes[heap] = code_prefix
    else:
        # Recursively create binary codes for edges between left and right trees/heaps
        left, right = heap
        heap_codes(left,  code_prefix + "1", codes)
        heap_codes(right, code_prefix + "0", codes)

    return codes

#################################################################################

'''Matthew'''
# a)
# Input: frequency_table(st)
# Output:
# Character Frequencies:
# 'a': 1
# 'b': 2
# 'c': 3
# 'd': 4
def frequency_table(st):
    table = {}
    for i in st:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1

    print("Character Frequencies:")
    for i in sorted(table.items()):
        print(f"'{i[0]}': {str(i[1])}")
    return table

'''Dennis'''
# b)
# Input: Huffman_code(st)
# Output:
# Huffman Codes:
# 'a': 000
# 'b': 001
# 'c': 01
# 'd': 1
def Huffman_code(st):
    st = st.lower()
    freq_table = frequency_table(st)
    heap = into_minheap(freq_table)
    flip = len(heap) - 2

    while len(heap) > 1:
        # Left tree is first pop from minheap and right tree is second pop from minheap
        left_tree, left_freq = pop_minheap(heap)
        right_tree, right_freq = pop_minheap(heap)

        # Handle first merge being in reverse
        if len(heap) == flip:
            merged_tree = (right_tree, left_tree)
        else:
            merged_tree = (left_tree, right_tree)
        merged_freq = left_freq + right_freq

        insert_minheap(heap, (merged_tree, merged_freq))

    tree = heap[0][0]
    codes = heap_codes(tree)

    #print(tree)
    print("\nHuffman Codes:")
    for ch in sorted(codes):
        print(f"'{ch}': {codes[ch]}")

    # Convert dictionary of codes to list of tuples
    codes = list(codes.items())

    return codes

'''Dennis'''
# c)
# Input: Huffman_encode(st, codes)
# Output:
# Encoded String:
# 0000010010010101011111
def Huffman_encode(st, codes):
    st = st.lower()
    code_dict = dict(codes)

    bst = "".join(code_dict[ch] for ch in st)
    print("\nEncoded String:\n" + bst)

    return bst

'''Yonghyeon'''
# d)
# Input: Huffman_tree(L)
# Output:
# (Huffman tree structure is constructed and stored in variable `tree`)
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

'''Yonghyeon'''
# e)
# Input: Huffman_decode(bst, tree)
# Output:
# Decoded String:
# abbcccdddd
def Huffman_decode(bst, tree):
    result = ''
    node = tree
    for bit in bst:
        node = node[bit]
        if 'char' in node:
            result += node['char']
            node = tree  # 다시 루트로 리셋
    print("\nDecoded String:")
    print(result)

#################################################################################
# Given examples:

st = "abbcccdddd"
L = [('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')]
bst = "0000010010101011111"

st2 = "This is a test for the created functions."

# Output

print("Input String:\n" + st + "\n")
# a) & b)
# b) Huffman_code(st) calls a) frequency_table(st)
codes = Huffman_code(st)
# c)
Huffman_encode(st, codes)
# d)
tree = Huffman_tree(codes)
# e)
Huffman_decode(bst, tree)