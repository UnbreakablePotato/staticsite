import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode(".", TextType.PLAIN_TEXT)
        self.assertNotEqual(node, node2)
    def test_url(self):
        node = TextNode("facebook", TextType.LINK, "http://www.facebook.com")
        self.assertIsNotNone(node.url)
    def test_url_none(self):
        node = TextNode("x", TextType.LINK)
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()