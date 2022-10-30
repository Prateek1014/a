import xml.etree.ElementTree as ET

tree=ET.parse('orders.xml')

root=tree.getroot()

print(root.tag)
