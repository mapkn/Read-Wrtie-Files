# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:23:03 2018

@author: patemi
"""

# Reference
# https://docs.python.org/2/library/xml.etree.elementtree.html


#ElementTree represents the whole XML document as a tree, and Element represents a single node in this tree

import xml.etree.ElementTree as ET


#tree = ET.parse('\\\\apw-grskfs01\\GVAR2\\Global Risk Management\\FRTB\\Index Decomposition\\DRC Messages\\CDS Index\\20906132.xml')
# tree = ET.parse('\\\\apw-grskfs01\\GVAR2\\Global Risk Management\\FRTB\\Index Decomposition\\DRC Messages\\EquityIndexOption\\EquityIndexOption.xml')
#tree = ET.parse('Sample.xml')
tree = ET.parse('100001391154_1EM GH.xml')

root = tree.getroot()

# As an Element, root has a tag and a dictionary of attributes:
#print(root.tag)
#print(root.attrib)


# It also has children nodes over which we can iterate:
for child in root:
    print (child.tag, child.attrib)
    
# Element has some useful methods that help iterate recursively over all the sub-tree below it 

for neighbor in root.iter():
     print (neighbor.tag, neighbor.attrib)

for neighbor in root.iter('ShockRecord'):
     print (neighbor.tag, neighbor.attrib)


#Element.findall() finds only elements with a tag which are direct children of the current element

for country in root.findall('country'):
     rank = country.find('rank').text
     name = country.get('name')
#     print (name, rank)

# Element.find() finds the first child with a particular tag
#ctry =root.find('country')
#rank = ctry.find('rank').text
#name = ctry.get('name')
#print (name, rank)
    
    
    
#for position in root.iter('Position'):
#     print(position.attrib)
    
#for callorput in root.iter('callorput'):
#     print(callorput.attrib)



