class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props = self.props
        props_list = []
        for p in props.keys():
            prop_string = f" {p}='{props[p]}'"
            props_list.append(prop_string)
        return "".join(props_list)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"