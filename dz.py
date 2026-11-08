
import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)

    heap = []

    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    if not heap:
        return None

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def build_codes(root):
    codes = {}

    def generate_codes(node, code):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = code if code else "0"
            return

        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    generate_codes(root, "")
    return codes


def encode(text, codes):
    return "".join(codes[char] for char in text)


def decode(encoded_text, root):
    if root is None:
        return ""

    if root.char is not None:
        return root.char * len(encoded_text)

    result = ""
    current = root

    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            result += current.char
            current = root

    return result


def main():
    with open("text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    if not text:
        print("Файл порожній!")
        return

    frequency = Counter(text)

    print("Частота символів:")
    for char, freq in frequency.items():
        print(repr(char), ":", freq)

    root = build_huffman_tree(text)

    codes = build_codes(root)

    print("\nКоди Хаффмана:")
    for char, code in codes.items():
        print(repr(char), ":", code)

    encoded_text = encode(text, codes)

    print("\nЗакодований текст:")
    print(encoded_text)

    decoded_text = decode(encoded_text, root)

    print("\nДекодований текст:")
    print(decoded_text)

    print("\nРезультат перевірки:")
    print("Тексти однакові:", text == decoded_text)


if __name__ == "__main__":
    main()
