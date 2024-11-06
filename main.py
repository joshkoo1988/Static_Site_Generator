from textnode import *

def main():
    testnode1 = TextNode("Hello",TextType.BOLD)
    testnode2 = TextNode("World",TextType.NORMAL,"http://example.com")

    print(testnode1)
    print(testnode2)
main()

