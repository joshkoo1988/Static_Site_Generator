

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_to_html_string = ""
        if self.props == None:
            return props_to_html_string
        else:
            for key in self.props:
                props_to_html_string += f' {key}="{self.props[key]}"'
        return props_to_html_string

    def __repr__(self):
        return f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,children=[],props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leafnodes must have a value.")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            props_list = ""
            for prop in self.props:
                props_list += f' {prop}="{self.props[prop]}"'
            return f"<{self.tag}{props_list}>{self.value}</{self.tag}>"