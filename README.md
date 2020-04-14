# mkdown2ReStructuredText
将 mkdown 文档转换成 ReStructuredText 文档

## 转换规则

目前支持的语法有：标题、斜体、粗体、超链接、图片、行内代码块、代码块。
但是某些语法不会完全对应：

- 标题：
    - h1 -> `===`
    - h2 -> `---`
    - h3 -> `^`
    - h4-h5 -> `'`
- 粗斜体会被替换成粗体

## 使用方法
`mkdown2ReStructuredText`有两个转换方法：

- convert_from_dir(source_dir, dest_dir)
- convert_from_file(source_file, dest_dir)

*source_dir*、*source_file*与*dest_dir*使用的都是绝对路径。

`example.py`提供了一个使用的例子。

**注意**：该脚本会将已存在的目的文件（filename.rst）覆盖。

路径中存在中文时可能需要解码：

``` python
c = mkdown2ReStructuredText.mkdown2ReStructuredText()
c.convert_from_dir('D:/mkdocs/work/docs/虚拟机转换'.decode('utf-8'),
                   'D:\AtomDoc\docs\source\Operation\Vm_convert')
c.convert_from_file('D:/mkdocs/work/docs/虚拟机转换/virt-p2v介绍.md'
                     .decode('utf-8'),
                     'D:\AtomDoc\docs\source\Operation\Vm_convert')
```
