 
from lxml import etree 
import os
 
 
def createFile(oripath):
    xml_list = os.listdir(path)
    for i in xml_list:  # 遍历所有xml文件
        fullPath = oripath + i  # 完整路径
        remove_(fullPath)  # 将完整路径作为参数传入调用该函数
 
 
def remove_(path):  # path 是原来xml文件的完整路径

    labName = ['aeroplane','bicycle','bird','boat','bottle','chair','diningtable','pottedplant','sofa','train','tvmonitor']
    tree = etree.parse(path)
    for i in tree.iter():  # i是该xml中的所有标签        
        if i.tag == "object":  # 找到为object的tag
            for j in labName:
                if i.find("name").text == j:             
                    parent = i.getparent()
                    parent.remove(i)
    Topath = r'MyNewXML\\' #生成新xml所在的文件夹路径
    tree.write(Topath + path.split('\\')[-1], encoding='utf-8') #将tree写入新的文件
 

 
if __name__ == '__main__':
    path = r'Myyolo\\MyXML\\' #你要处理的xml文件所在的文件夹路径
    createFile(path)