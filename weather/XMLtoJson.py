import sys
import xml.etree.ElementTree as ET
import json


def main():
    if(len(sys.argv)) != 2:
        print("Usage : XMLtoJson [filename.xml]")
        exit()
    file = sys.argv[1]
    print(file)
    tree = ET.parse(file)
    root = tree.getroot()
    data = travel(root)
    
    jsonj = json.dumps(data[root.tag])
    f = open(file[:-4]+".json", "w")
    f.write(jsonj)
    f.close()

def travel(node):
    data = dict() 
    if len(node.attrib)!=0:
        data.update(node.attrib)
    if node.text is not None:        
        if(node.text.strip()!= "") :
            return {node.tag:node.text}
            # print(node.text)
    for child in node:
        data.update(travel(child))
    return {node.tag:data}        
main()

