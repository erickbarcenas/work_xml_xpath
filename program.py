import xml.etree.ElementTree as ET

tree = ET.parse('bookstore.xml')
root = tree.getroot()

for child in root.findall("book"):
    title = child.find("title").text
    price = child.find("price").text

    print(f"title: {title}")
    print(f"price: {price}")