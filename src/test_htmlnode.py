import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
   def test_toHtml_excep(self):
      node = HTMLNode()
      self.assertRaises(NotImplementedError, node.to_html)

   def test_propToHtml(self):
      node = HTMLNode(props={
                      "href": "https://www.google.com",
                      "target": "_blank"
      })
      self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

class TestLeafNode(unittest.TestCase):
   def test_toHtml(self):
      node = LeafNode(tag="p", value="This is a paragraph of text!")
      self.assertEqual(node.to_html(), "<p>This is a paragraph of text!</p>")
      node2 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
      self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')


   def test_noValuefail(self):
      node = LeafNode()
      self.assertRaises(ValueError, node.to_html)


if __name__== "__main__":
   unittest.main()
