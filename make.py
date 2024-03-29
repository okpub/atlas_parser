#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import json
import os
import re
from PIL import Image

root_dir="."

def dirof(name):
    return root_dir+"/"+name

## 获取系统参数
def argv(n):
    if len(sys.argv)>n:
        return sys.argv[n]
    return None

## 递归建立目录
def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)   #os.mkdir(path)

## 保存图片
def save_img(img, name, prefix):
    # mkdir (去掉空格和最后的\)
    mkdir(prefix.strip().rstrip("\\"))
    # save 保存路径为py执行的路径
    img.save(prefix+name,'PNG')

## 从原始图片裁剪
def crop_img(img, x, y, w, h):
    return img.crop((x, y, x+w, y+h))

def item_handle(img, name, item, meta):
    frame=item["frame"]
    sourceSize=item["sourceSize"]               #原始尺寸(no used)
    spriteSourceSize=item["spriteSourceSize"]   #精灵的原始大小(no used)
    new_img=crop_img(img, frame["x"], frame["y"], frame["w"], frame["h"])
    save_img(new_img, name, meta["prefix"])
    print("     save img: "+name)

def atlas_dump(data):
    meta=data["meta"]
    img=Image.open(dirof(meta["image"])) #获取目录的图片
    for name in data["frames"]:
        item_handle(img, name, data["frames"][name], meta)


#合法解析的文件类型
legal_types=r'.+(.atlas|.json|.plist)$'

## 读取某个atlas文件
def load(path):
    #file=os.path.splitext(file)
    #filename,type=file #print(" file suffix: "+type, " file name: "+filename)
    if re.match(legal_types, path, re.I):
        print("load file: "+path)
        with open(path, "r") as txt:
            data = json.load(txt)
        #print(data)
        atlas_dump(data)
    else:
        print "the file of illegal : "+path



## 目录读取
def load_dir(path):
    print("load dir: "+path)
    for file in os.listdir(path):
        if os.path.isdir(file): #忽略子目录的文件
            print("#####ERROR: child file not parsing ["+file+"]")
        else:
            load(dirof(file))

# main   load("createUI.atlas") #可以读取某个atlas/json文件
if __name__=='__main__':
    path=argv(1)
    if not path:
        load_dir(root_dir)       #默认路径
    else:
        if os.path.isdir(path):
            root_dir=path
            load_dir(path)  #指定目录(输出为本目录)
        else:
            root_dir=os.path.dirname(path)
            load(path)      #指定文件
