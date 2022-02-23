#!/usr/bin/python

import sys
from lxml import etree as ET

def find(filename, xpath):
    tree = ET.parse(f"{filename}")
    root = tree.getroot()

    for element in tree.xpath(f"{xpath}"):
        print(element.text)


if len(sys.argv) == 3:
    data = list(sys.argv)

    filename = data[1]
    xpath = data[2]

    print("-------------------------------")

    print(f"filename: {filename}")
    print(f"xpath: {xpath}")

    print("-------------------------------")

    find(filename, xpath)

else:
    print("The number of arguments is invalid, please check the documentation!")

