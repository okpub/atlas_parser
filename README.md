# atlas图集还原神器

### 安装python2.7图像库配置 (本教程以mac为例)

1 安装pip

```vim
brew install pip
```

2 安装图像处理模块

```vim
sudo pip install pillow
sudo pip install image
```

3 终端测试(无报错则成功)

```vim
python
from PIL import Image
```

### 使用make.py（打开mac终端）
ps：有效文件后缀(*.atlas | *.json | *.plist)

1 默认本目录
```vim
python make.py
```

2 指定文件
```vim
python make.py test.atlas
```

3 指定路径
```vim
python make.py path
```

### END
