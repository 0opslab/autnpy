封装常用的操作，方便开发使用

## 安装方法
```
python setup.py install

python setup.py clean --all
```

## 使用方法
```python
from Autnpy import Autnpy

print(Autnpy.base_path())
print(Autnpy.trim_path("c:\\files\\\\file2//files"))
print(Autnpy.base_path("c:\\files\\\\file2//files"))
print(Autnpy.base_path("/str/test.txt"))

```