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