class HTMLNode:
    def __init__(self, 
                 tag: str | None = None, 
                 value: str | None = None, 
                 children = None,
                 props: dict[str, str] | None = None
                 ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            return "".join(map(lambda kv: f' {kv[0]}="{kv[1]}"', self.props.items()))
        return ""
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str | ValueError:
        if self.value == "" or self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str | ValueError:
        if self.tag == "" or self.tag == None:
            raise ValueError("Missing Tag")
        if self.children == None:
            raise ValueError("Missing Children")
        children_html = "".join(list(map(lambda x: x.to_html(), self.children)))
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"