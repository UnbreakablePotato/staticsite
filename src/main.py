from textnode import TextNode
from textnode import TextType

def main():
    new_obj = TextNode("This is some text", TextType.LINK, "http://suckmytoes.com")
    print(new_obj)

main()