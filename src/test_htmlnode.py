import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_propstohtml(self):
        test_node = HTMLNode(props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(test_node.props_to_html(), expected)

    def test_print(self):
        test_node = HTMLNode(tag="test",children=[])
        expected = "tag = test, value = None, children = [], props = None"
        self.assertEqual(str(test_node),expected)

    def test_emptyprop(self):
        test_node1 = HTMLNode(props={})
        self.assertEqual(test_node1.props_to_html(),"")


if __name__ == "__main__":
    unittest.main()