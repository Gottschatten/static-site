import unittest
from textnode import TextNode

class TestNodeText(unittest.TestCase):
   def test_eq(self):
      node  = TextNode("This is a TextNode!", "bold")
      node2 = TextNode("This is a TextNode!", "bold")
      self.assertEqual(
         node,
         node2
      )
      
   def test_ueq_noUrl(self):
      node = TextNode("This is a TextNode!", "bold", "http://taucherglocke.dev/")
      node2 =TextNode("THis is a TextNode!", "bold")
      self.assertNotEqual(
            node,
            node2
      )

if __name__ == "__main__":
   unittest.main()
