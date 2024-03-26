class HTMLNode:
   def __init__(self, tag = None, value = None, children = None, props = None ) -> None:
      self.tag = tag
      self.value = value
      self.children = children
      self.props = props

   def to_html(self):
      raise NotImplementedError

   def props_to_html(self):
      if self.props == None:
         return ""
      html = ""
      for prop in self.props:
         html += f' {prop}="{self.props[prop]}"'
      return html

class LeafNode(HTMLNode):
   def __init__(self, tag=None, value=None, children=None, props=None) -> None:
      super().__init__(tag, value, children, props)

   def to_html(self):
      if self.value is None:
         raise ValueError
      if self.tag is None:
         return self.value
      if self.props is None:
         html = f"<{self.tag}>" + self.value + f"</{self.tag}>"
         return html
      html = f'<{self.tag}{self.props_to_html()}>' + self.value + f'</{self.tag}>'
      return html

