# laya/cocos图集神器

### python环境
(利用python2.7处理图像 PS: 以mac为例, windows教程网络自取)

1 安装pip步骤

```vim
brew install pip
```

2 安装pip后还需要导入图像处理模块

```vim
sudo pip install pillow
sudo pip install image
```

3 终端测试,如果无报错则成功

```vim
python
from PIL import Image
```

### 使用make.py将图集还原
1 默认本目录所有图集
```vim
python make.py
```

2 指定单独文件(*.atlas | *.json | *.plist)
```vim
python make.py test.atlas
```

3 指定路径
```vim
python make.py path
```
