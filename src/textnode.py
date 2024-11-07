from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def format_text(self):
        match self.text_type:
            case TextType.NORMAL:
                return self.text
            case TextType.BOLD:
                return self.text
            case TextType.ITALIC:
                return self.text
            case TextType.CODE:
                return self.text
            case TextType.LINK:
                return self.text
            case TextType.IMAGE:
                return self.text
            case _:
                raise ValueError(f"Invalid text type : {self.text}")



    def __eq__(self,other):
        if isinstance(other,TextNode):
            return (self.text == other.text and
                    self.text_type == other.text_type and
                    self.url == other.url)
        return False
    
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type},{self.url})"