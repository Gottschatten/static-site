from htmlnode import LeafNode



text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

    
class TextNode:
    def __init__(self, text, text_type, url = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other ) -> bool:
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def text_node_to_html(self):
        check = False
        value = self.text
        props = None
        tag = None
        if self.text_type is text_type_text:
            check = True
        if self.text_type is text_type_bold:
            tag = "b"
            check = True
        if self.text_type is text_type_italic:
            tag = "i"
            check = True
        if self.text_type is text_type_code:
            tag = "code"
            check = True
        if self.text_type is text_type_link:
            tag = "a"
            props = {"href" : f"{self.url}"}
            check = True
        if self.text_type is text_type_image:
            tag = "img"
            props = {"src": f" {self.url}", "alt": f"{self.text}"}
            value = ""
            check = True
        if check:
            return LeafNode(tag,value,props).to_html()
        raise ValueError(f"Invalid text type: {self.text_type}")


    def __repr__(self) -> str:
       return f'TextNode({self.text}, {self.text_type}, {self.url})'
