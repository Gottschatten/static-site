import unittest
from htmlnode import HTMLNode

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


if __name__== "__main__":
   unittest.main()