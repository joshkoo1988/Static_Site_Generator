import unittest
from htmlnode import *


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

    def test_print(self):
        test_node1 = LeafNode(tag="a",value="this is a test")
        self.assertEqual(test_node1.to_html(),'<a>this is a test</a>')

    def test_tohtml_novalue(self):
        test_node1 = LeafNode(None,"test")
        self.assertEqual(test_node1.to_html(),test_node1.value)

    def test2_tohtml(self):
        test_node1 = LeafNode("p","test",{"test":"test1"})
        self.assertEqual(test_node1.to_html(),
                         '<p test="test1">test</p>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()