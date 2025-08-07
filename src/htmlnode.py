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