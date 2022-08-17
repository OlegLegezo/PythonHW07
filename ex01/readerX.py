import os

path = os.path.join('PythonHW07', 'ex01', 'output.csv')
with open(path, 'r') as f:
    text = f.read()
data1 = text.split()
print(data1)
