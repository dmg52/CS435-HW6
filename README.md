# CS435-HW6
# Assignment Details
Homework assignment 6 for CS435

You are given a text of at most 256 characters. Implement the following functions as part of this assignment:

a) **`frequency_table(st)`**
Write a function `frequency_table(st)` that constructs a frequency table for each character in the string `st` and prints it.
Input: A string `st` with a maximum length of 256 characters.
Output: Print each character along with its corresponding frequency.

b) **`Huffman_code(st)`**
Write a function `Huffman_code(st)` that builds a Huffman tree from the string `st` and generates the Huffman codes for each character. Print each character with its corresponding code.
Input: A string st with a maximum length of 256 characters.
Output: Print the Huffman code for each character in the string.

c) **`Huffman_encode(st,codes)`**
Write a function `Huffman_encode(st,codes)` that prints the binary encoded version of `st`, based on the Huffman codes generated in part (b) `codes`.
Input: A string `st` with a maximum length of 256 characters and its Huffman codes `codes`.
Output: Print the binary-encoded string using the Huffman codes.

d) **`Huffman_tree(L)`**
You are given a list `L` of characters and their corresponding Huffman codes. Write a function `Huffman_tree(L)` that constructs a Huffman tree based on this list.
Input: A list `L` of characters and their corresponding Huffman codes.
Output: Return the Huffman tree constructed from the list.

e) **`Huffman_decode(bst,tree)`**
Using the Huffman tree built in part (d), write a function `Huffman_decode(bst,tree)` to decode the binary-encoded text `bst` back into its original string.
Input: A binary-encoded string `bst` and its Huffman tree `tree`.
Output: Print the decoded string.

# Run Program
Example uses the following inputs:
`st = "abbcccdddd"`
`L = [('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')]`
`bst = "0000010010101011111"`

To run, simply run in IDE.
