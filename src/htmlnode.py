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
   def __init__(self, tag=None, value=None, props=None) -> None:
      super().__init__(tag, value, None, props)

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

class ParentNode(HTMLNode):
   def __init__(self, tag, children, props=None)  -> None:
      self.tag = tag
      self.props = props
      self.children = children

   def to_html(self):
      if self.tag is None:
         raise ValueError("No Tag specified")
      if self.children is None: 
         raise ValueError("No Children specified")
      html = f"<{self.tag}>"
      for node in self.children:
         html =html + node.to_html()
      html =html + f"</{self.tag}>"
      return html
