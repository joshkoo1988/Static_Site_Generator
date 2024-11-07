import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_empty_string(self):
        empty_string_node = TextNode("",TextType.NORMAL)
        self.assertEqual(empty_string_node.text, "")
        self.assertEqual(empty_string_node.text_type, TextType.NORMAL)

    def test_wrong_text_type(self):
        with self.assertRaises(ValueError):
            wrong_text_node = TextNode("blah",TextType("IDONTEXIST"),"blah.com")
            wrong_text_node.format_text()
        
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD,"www.blah.com")
        node2 = TextNode("This is a text node", TextType.BOLD,"www.blah.com")
        self.assertEqual(node,node2)

    def test_eq3(self):
        node = TextNode("This is a node", TextType.BOLD,None)
        node2 = TextNode("This is a node", TextType.BOLD)
        self.assertEqual(node,node2)

if __name__ == "__main__":
    unittest.main()