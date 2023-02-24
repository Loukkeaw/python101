Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shap('turte')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tao.shap('turte')
AttributeError: 'Turtle' object has no attribute 'shap'. Did you mean: 'shape'?
tao.shape('turte')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tao.shape('turte')
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named turte
tao = turtle.Pen()
tao.shape('turtle')
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
>>> tao.clear()
>>> for i in range(4): //repeting
SyntaxError: invalid syntax
>>> for i in range(4):
...     tao.forward(100)
...     tao.left(90)
... tao.clear()
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 

>>> SyntaxError: invalid syntaxfor i in range(4):
...     tao.forward(100)
...     tao.left(90)
... tao.clear()
SyntaxError: invalid syntax
>>> tao.clear
<bound method RawTurtle.clear of <turtle.Turtle object at 0x1027df390>>
>>> for i in range(4)
SyntaxError: incomplete input
>>> for i in range(4):
...     tao.forward(100)
...     tao.left.(90)
...     
SyntaxError: invalid syntax
>>> for i in range(4):
...     tao.forward(100)
...     tao.left(90)
... 

... 
... 
>>> 
>>> tao.penup()
>>> 
>>> tao.goto(200, 200)
