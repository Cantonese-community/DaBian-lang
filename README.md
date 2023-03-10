# The DaBian Programming language
💩"答辩"编程语言, 想掌握一门编程语言？不是"答辩"的我不学!  

## Hello World
```
捅了老挝 -> "Hello World!"
```
输出结果:  
```
Hello World!
```
运行成功后会自动"结算动画":  
![结算动画](examples/run-exmple.gif)
有了输出那一定就要有输入了, 可以用`本以为抓个小贼`或`抓个小贼`, 输出可以用`没想到捅了老挝`或`捅了老挝`:  
```
本以为抓个小贼 -> (num, "请输入一个数: ")
没想到捅了老挝 -> num
```
结果为:  
```
>>> 请输入一个数: 666
666
```

## 赋值语句
在"答辩"语言中, 所有对象都可以看作答辩. 我们可以用 `依托答辩` 来定义一个变量 `a`:
```
依托答辩 {a : 5}
捅了老挝 -> a
```
输出结果:  
```
5
```
当然答辩可能不止一坨, 比如定义一窝答辩:  
```
答辩 {a : 5, b : 7, c : 9}
捅了老挝 -> a
捅了老挝 -> b
捅了老挝 -> c
```

## 函数定义
对于违法行为我们要用 `功夫是这样的` 定义一个函数将其 `绳之以法`!  
`此地答辩`相当于`return`, 函数定义完后别忘了喊一句: `任何邪恶终将绳之以法!`:  
```
功夫是这样的 f(a, b) ->
    捅了老挝 -> (a + b)
    此地答辩
任何邪恶终将绳之以法!
```
调用函数:  
```
绳之以法 -> f (1, 3)
```
输出结果:  
```
4
```

## 循环
```
依托答辩 {白象 : 1}
不是 (白象) 的我不吃 ->
    捅了老挝 -> "看你往哪跑!"
因为是良心的中国制造!
```
## 条件语句
if-else语句:  
```
依托答辩 {num : 7}
要是 (num % 2 == 1) 跟我zs ->
    捅了老挝 -> "num 是奇数"
你这是违法行为 跟我zs ->
    捅了老挝 -> "num 是偶数"
任何邪恶终将绳之以法!
```

输出结果:  
```
num 是奇数
```
更多例子见 [这里](examples/).  
## 安装
"答辩"语言基于 [粤语编程语言](https://github.com/StepfenShawn/Cantonese) 开发, 所以直接用 `pip` 安装好 `Cantonese` 就行了:  
```
pip install Cantonese
```
再安装好几个播放"结算动画"要用到的库:  
```
pip install numpy
pip install pillow
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
```
运行:  
```
Cantonese src/dabian.cantonese [-文件名]
```
## 最后
在b站娱乐的同时也别忘了学习哦! Just for fun! Enjoy it!  
如果有更好的想法，欢迎提issue或PR!!!  
![Bye](dabian.gif)