import xml.etree.ElementTree as ET

tree = ET.parse('bookstore.xml')
root = tree.getroot()



def with_xpath():
    for child in root.findall("book"):
        title = child.find("title").text
        price = child.find("price").text

        print(f"title: {title}")
        print(f"price: {price}")

def get_title_price():
    for child in root.findall("//book/title"):
        
        print(child)


#get_title_price()


    
for child in root.findall("book/title | book/price"):
    print(f"child: {child.attrib}")